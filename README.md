# MIP engine Cookiecutter

Cookiecutter template for creating repost for Mixed-Integer Programming (MIP) project.  
This template provides a quick way to set up optimization problem repositories with a consistent structure.

## Requirements

- Python **3.13+**
- [cookiecutter](https://pypi.org/project/cookiecutter/) `>=2.6.0`
- [uv](https://github.com/astral-sh/uv)

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
``