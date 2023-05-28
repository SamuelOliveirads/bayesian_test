# Pipeline

> *Note:* This is a `README.md` boilerplate generated using `Kedro 0.18.6`.

## Overview

This pipeline:

1. Runs a flask application and a scrapper in parallel using multithreading (`run_flask_app_and_scrapper` node in `nodes.py`).
2. Animates a plot of the data experiment (`animate_plot` node in `analytics.py`).

## Pipeline inputs

### `data_experiment`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | DataFrame representing the experimental data to be passed to the flask application and the scrapper |

## Pipeline intermediate outputs

### `data_experiment_updated`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | Updated DataFrame after running the flask application and scrapper |

### `data_experiment_output`

|      |                    |
| ---- | ------------------ |
| Type | `pandas.DataFrame` |
| Description | Output DataFrame after running the flask application and scrapper |

## Pipeline outputs

### `None`

*Note: The `animate_plot` function does not produce any explicit output. It generates an animated plot as a side effect.*
