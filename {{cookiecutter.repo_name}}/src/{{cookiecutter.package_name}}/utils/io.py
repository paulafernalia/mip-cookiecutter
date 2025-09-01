import json
from pathlib import Path
from typing import Union

import yaml

from {{cookiecutter.package_name}}.data.models import ModelData
from {{cookiecutter.package_name}}.optimization.parameters import Parameters


def load_data_from_json(path: Union[str, Path]) -> ModelData:
    """Load data from json and validate it."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return ModelData.model_validate(data)


def load_parameters_from_yaml(file_path: str) -> Parameters:
    """Load solver parameters from a YAML configuration file.

    The YAML file should contain keys corresponding to Parameters:

    - time_limit: Maximum solver runtime in seconds (int)
    - mip_rel_gap: Relative gap tolerance for MIP solver (float)
    - verbose: Whether to enable verbose logging (bool)

    Parameters
    ----------
    file_path : str
        Path to the YAML configuration file.

    Returns
    -------
    Parameters
        A Pydantic model instance containing the solver parameters.

    Raises
    ------
    FileNotFoundError
        If the YAML file does not exist.
    yaml.YAMLError
        If the YAML file cannot be parsed.
    """
    with open(file_path, "r") as f:
        cfg = yaml.safe_load(f)
    return Parameters(**cfg)
