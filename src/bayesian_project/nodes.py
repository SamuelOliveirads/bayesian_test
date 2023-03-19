"""
This is a boilerplate pipeline
generated using Kedro 0.18.6
"""

import logging
from typing import Any, Dict, Tuple

import numpy as np
from flask import Flask, redirect, render_template, url_for

app = Flask(__name__, template_folder="../../data/01_raw")

def split_data(
    data: pd.DataFrame, parameters: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Splits data into features and target training and test sets.

@app.route("/home")
def index():
    if np.random.random() < 0.5:
        selected_template = render_template("pg_layout_blue.html")
    else:
        selected_template = render_template("pg_layout_red.html")
    return selected_template

    data_train = data.sample(
        frac=parameters["train_fraction"], random_state=parameters["random_state"]
    )
    data_test = data.drop(data_train.index)

@app.route("/yes", methods=["POST"])
def yes_event():
    return redirect(url_for("index"))


@app.route("/no", methods=["POST"])
def no_event():
    return redirect(url_for("index"))


def run_flask_app():
    app.run()

def make_predictions(
    X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series
) -> pd.Series:
    """Uses 1-nearest neighbour classifier to create predictions.

    Args:
        X_train: Training data of features.
        y_train: Training data for target.
        X_test: Test data for features.

    Returns:
        y_pred: Prediction of the target variable.
    """

    X_train_numpy = X_train.to_numpy()
    X_test_numpy = X_test.to_numpy()

    squared_distances = np.sum(
        (X_train_numpy[:, None, :] - X_test_numpy[None, :, :]) ** 2, axis=-1
    )
    nearest_neighbour = squared_distances.argmin(axis=0)
    y_pred = y_train.iloc[nearest_neighbour]
    y_pred.index = X_test.index

    return y_pred


def report_accuracy(y_pred: pd.Series, y_test: pd.Series):
    """Calculates and logs the accuracy.

    Args:
        y_pred: Predicted target.
        y_test: True target.
    """
    accuracy = (y_pred == y_test).sum() / len(y_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has accuracy of %.3f on test data.", accuracy)
