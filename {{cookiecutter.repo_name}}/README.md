# {{cookiecutter.project_name}}

{{ cookiecutter.project_name }} implements as a Mixed-Integer Programming (MIP) using HiGHS.

This project was generated using [mip-cookiecutter](https://github.com/your-username/mip-cookiecutter).

This template encourages good development practices:

- Unit tests: The tests/ folder provides a starting point for testing your MIP models and code.
- Pre-commit checks: A pre-commit configuration ensures your code passes:
    - mypy (type checking)
    - bandit (security checks)
    - ruff (linting)
    - complexipy (complexity analysis)
- Continuous Integration: GitHub Actions run tests, linters, and other checks on push to ensure code quality.

## Project structure

```text
.
├── LICENSE
├── Makefile
├── README.md
├── conf
│   ├── logging.yml
│   └── parameters.yaml
├── data
│   └── instance.json
├── notebooks
├── pyproject.toml
├── src
│   └── {{ cookiecutter.package_name }}
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
- Python 3.13+
- [`uv`](https://github.com/astral-sh/uv)

If you don't have `uv` installed, you can follow the intructions in the uv [documentation](https://docs.astral.sh/uv/getting-started/installation/). Make sure `uv` is on your `PATH`.

## Set up

Install dependencies with:
```
uv sync --dev
```


## Usage

This project uses a `Makefile` to simplify running the most used commands on **Linux** and **macOS**.

Install the `orproject` as an editable package with

```
make install
```

To run the flow in `{{cookiecutter.package_name}}/__main__.py`:

```
make run
```


Run tests with:
```
make test
```

Format code with
```
make ruff
```

To install and run hooks:
```
make hooks
``
