# MIP engine Cookiecutter

Cookiecutter template for creating repost for Mixed-Integer Programming (MIP) project.  
This template provides a quick way to set up optimization problem repositories with a consistent structure.

## Template structure

## Project structure

```text
.
├── LICENSE
├── Makefile
├── README.md
├── .gitignore
├── conf
│   ├── logging.yml
│   └── parameters.yaml
├── data
│   └── instance.json
├── .github
│   └── workflows
│       └── ci-cd.yml    
├── notebooks
├── pyproject.toml
├── src
│   └── <package_name>
│       ├── __init__.py
│       ├── __main__.py
│       ├── data
│       │   └── models.py
│       ├── optimization
│       │   ├── constraints.py
│       │   ├── model_builder.py
│       │   ├── parameters.py
│       │   ├── solver.py
│       │   ├── types.py
│       │   └── variables.py
│       └── utils
│           └── io.py
└── tests
```

## Requirements

- Python **3.13+**
- [cookiecutter](https://pypi.org/project/cookiecutter/) `>=2.6.0`

## Usage

Install dependencies with:

```bash
pip install cookiecutter>=2.6.0
```

Generate a new MIP project from this template
```
cookiecutter https://github.com/paulafernalia/mip-cookiecutter.git
```

You will be prompted for values defined in `cookiecutter.json`:

```
{
    "repo_name": "knapsack-mip-solver",
    "project_name": "Knapsack Problem",
    "package_name": "knapsack",
}
```