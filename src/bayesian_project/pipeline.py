"""
This is a boilerplate pipeline
generated using Kedro 0.18.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import run_flask_app_and_scrapper
from .analytics import animate_plot


def create_pipeline(**kwargs) -> Pipeline:
    scrapping_pipeline = pipeline(
        [
            node(
                func=run_flask_app_and_scrapper,
                inputs="data_experiment",
                outputs=["data_experiment_updated", "data_experiment_output"],
                name="run_flask_app_and_scrapper",
            ),
        ]
    )
    analysis_pipeline = pipeline(
        [
            node(func=animate_plot, 
                inputs="data_experiment", 
                outputs=None, 
                name="animate_plot"),
        ])
    return scrapping_pipeline + analysis_pipeline
