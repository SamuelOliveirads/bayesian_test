"""
This is a boilerplate pipeline
generated using Kedro 0.18.6
"""
import os
import threading
import time

import numpy as np
from flask import Flask, redirect, render_template, url_for
from selenium import webdriver

app = Flask(__name__, template_folder="../../data/01_raw")


@app.route("/home")
def index():
    if np.random.random() < 0.5:
        selected_template = render_template("pg_layout_blue.html")
    else:
        selected_template = render_template("pg_layout_red.html")
    return selected_template


@app.route("/yes", methods=["POST"])
def yes_event():
    return redirect(url_for("index"))


@app.route("/no", methods=["POST"])
def no_event():
    return redirect(url_for("index"))


def run_flask_app():
    app.run()


def run_scrapper():
    time.sleep(2)  # Give Flask server some time to start
    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/home")

    clicks = 10000
    for click in range(clicks):
        if np.random.random() < 0.5:
            driver.find_element("name", "yescheckbox").click()
            driver.find_element("id", "yesbtn").click()
        else:
            driver.find_element("name", "nocheckbox").click()
            driver.find_element("id", "nobtn").click()

    driver.quit()
    return None


def run_flask_app_and_scrapper(example_iris_data):
    flask_thread = threading.Thread(target=run_flask_app)
    scraper_thread = threading.Thread(target=run_scrapper)

    flask_thread.start()
    scraper_thread.start()

    scraper_thread.join()
    # Terminate Flask app when the scraper is finished
    # You can replace this with a more graceful shutdown method if needed
    os._exit(0)
