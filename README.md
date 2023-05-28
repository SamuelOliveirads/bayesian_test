# bayesian_project

## Overview

This is your new Kedro project, which was generated using `Kedro 0.18.6`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

### Bussiness Problem
The company iSketch, located in São Paulo, manufactures and makes available software focused on the 3D development of projects for civil construction, as a way of prototyping large projects.

To use the software, the customer needs to acquire a license that is renewed annually.

One of iSketch's best customer acquisition strategies is to capture the customer's email address in exchange for a newsletter with weekly content about construction. The newsletter subscription allows you to start a relationship between iSketch and people, in order to show the advantages of using the software to create civil construction prototypes.

Therefore, improving the conversion rate of the email capture page by offering the newsletter in return is crucial for growing the number of customers.

Therefore, the Marketing Coordinator of the company asked the design team to create a new email capture page with a small change in the colors of the 'sign-up' button, in order to increase the conversion rate of the page.

The design team created a page with a red sign-up button to be tested against the current page that has a blue sign-up button. The Marketing Coordinator is in a hurry to test the new page, as the company has been acquiring few customers in recent weeks and this could jeopardize the company's annual revenue.

The iSketch Data Scientist team was added with the mission to test the new email capture page as soon as possible. The first idea was to plan an A/B test experiment between the two pages for a period of 7 days, to conclude the effectiveness of the button color change. However, the Marketing Coordinator categorically told the data team that they could not wait 7 days and asked them to complete it in less time.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run --runner=ParallelRunner
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
