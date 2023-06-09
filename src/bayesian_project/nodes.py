"""
This is a boilerplate pipeline
generated using Kedro 0.18.6
"""
import threading
import time

import numpy as np
import pandas as pd
from flask import Flask, redirect, render_template, request, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

temp_df = None


def _update_experiment_data(click: int, visit: int, group: str):
    global temp_df

    df_raw = pd.DataFrame({"click": [click], "visit": [visit], "group": [group]})
    temp_df = pd.concat([temp_df, df_raw], ignore_index=True)
    return None


def run_flask_app(data_experiment: pd.DataFrame) -> None:
    """
    Launches a Flask server that displays two different versions of a website,
    according to a random probability. The server also logs user clicks and updates
    the 'temp_df' DataFrame with these clicks.

    Parameters
    ----------
    data_experiment : pd.DataFrame
        Initial DataFrame to be updated with user clicks.

    """
    global temp_df
    temp_df = data_experiment
    app = Flask(__name__, template_folder="../../data/01_raw")

    @app.route("/")
    def base_route():
        """
        Base route that redirects to the index page.
        """
        return redirect(url_for("index"))

    @app.route("/home")
    def index():
        """
        Index page route. Selects and renders a template based on a random condition.
        """
        if np.random.random() < 0.3:
            selected_template = render_template("pg_layout_blue.html")
        else:
            selected_template = render_template("pg_layout_red.html")
        return selected_template

    @app.route("/yes", methods=["POST"])
    def yes_event():
        """
        Route for the 'yes' event. Updates the experiment data and
        redirects to the index page.
        """
        _update_experiment_data(click=1, visit=1, group="control")

        return redirect(url_for("index"))

    @app.route("/no", methods=["POST"])
    def no_event():
        """
        Route for the 'no' event. Updates the experiment data and
        redirects to the index page.
        """
        _update_experiment_data(click=1, visit=0, group="control")

        return redirect(url_for("index"))

    def shutdown_server():
        func = request.environ.get("werkzeug.server.shutdown")
        if func is None:
            raise RuntimeError("Not running with the Werkzeug Server")
        func()

    @app.route("/shutdown", methods=["POST"])
    def shutdown():
        """
        Route for shutting down the server.
        """
        shutdown_server()
        return "Server shutting down..."

    app.run()


def run_scrapper() -> None:
    """
    Starts a web scrapper that automates navigation on the website served by the
    Flask server. The scrapper 'clicks' on the "yes" or "no" buttons on the website,
    according to a random probability.
    """
    time.sleep(2)  # Give Flask server some time to start
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    driver.get("http://127.0.0.1:5000/home")

    clicks = 50
    for click in range(clicks):
        if np.random.random() < 0.3:
            driver.find_element("name", "yescheckbox").click()
            driver.find_element("id", "yesbtn").click()
            time.sleep(2)
        else:
            driver.find_element("name", "nocheckbox").click()
            driver.find_element("id", "nobtn").click()
            time.sleep(2)

    driver.quit()
    driver.get("http://127.0.0.1:5000/shutdown")
    driver.close()

    return None


def run_flask_app_and_scrapper(data_experiment: pd.DataFrame) -> pd.DataFrame:
    """
    Starts both the Flask server and the web scrapper concurrently.

    Parameters
    ----------
    data_experiment : pd.DataFrame
        Initial DataFrame to be updated with user clicks.

    Returns
    -------
    pd.DataFrame
        Updated DataFrame with new user clicks.

    """
    flask_thread = threading.Thread(target=run_flask_app, args=(data_experiment,))
    scraper_thread = threading.Thread(target=run_scrapper)

    flask_thread.start()
    scraper_thread.start()

    scraper_thread.join()

    global temp_df
    updated_df = temp_df.copy()

    return updated_df, updated_df
