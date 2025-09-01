# MIP engine Cookiecutter

Cookiecutter template for creating repos for Mixed-Integer Programming (MIP) related projects.  
This template provides a quick way to set up optimization problem repositories with a consistent structure. It focuses on good coding practices, but also includes some boilerplate code for loading, creating and solving MIPs.

## Template structure

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
│       │   ├── __init__.py
│       │   └── models.py
│       ├── optimization
│       │   ├── constraints.py
│       │   ├── model_builder.py
│       │   ├── parameters.py
│       │   ├── solver.py
│       │   ├── types.py
│       │   └── variables.py
│       └── utils
│           ├── __init__.py
│           └── io.py
└── tests
```

## Requirements

- Python **3.13+**
- [cruft](https://pypi.org/project/cruft/) `>=2.16.0`
- [cookiecutter](https://pypi.org/project/cookiecutter/) `>=2.6.0`


## Usage

This template can either be used with [Cookiecutter](https://pypi.org/project/cookiecutter/) or [Cruft](https://pypi.org/project/cruft/). Cookiecutter creates an one off instantiation of the original template but does not create any link to it. Cruft, built on top of Cookiecutter, automates the transfer of changes in the Cookiecutter template repo to the instantiated project.

### To set up a new repo with Cookiecutter

Install dependencies with:

```bash
pip install cookiecutter
```
Generate a new repo from this template
```
cookiecutter https://github.com/paulafernalia/mip-cookiecutter.git
```

### To set up a new repo with Cruft

Install dependencies with:

```bash
pip install cruft
```

Generate a new repo from this template
```
cruft create https://github.com/paulafernalia/mip-cookiecutter.git
```

These instructions will create an new folder with the files in the template. However, thees files will not have a repo associated with it. You can create it with:

```
git init -b main
git add .
git commit -m "Initial commit from template"
git remote add origin git@github.com:<username>/<repo>.git
git push -u origin main
```
