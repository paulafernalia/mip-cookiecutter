"""
Main module for {{cookiecutter.project_name}}.

This module provides an entry point for running the project
as a script. It simply prints a greeting message to the console.
"""

from {{cookiecutter.package_name}}.optimization.engine import Engine
from {{cookiecutter.package_name}}.utils.io import load_data_from_json, load_parameters_from_yaml


def main() -> None:
    """
    Run package directly.

    This function serves as the entry point when the package is run
    directly.
    """
    # data = load_data_from_json("data/instance.json")
    # params = load_parameters_from_yaml("conf/parameters.yaml")

    # solver = Engine(data)
    # solver.set_parameters(params)

    # solver.run()
    # solver.build_solution()


if __name__ == "__main__":
    main()
