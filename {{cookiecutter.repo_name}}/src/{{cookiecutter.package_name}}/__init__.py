"""Package initialization for {{cookiecutter.project_name}}."""

import logging
import logging.config
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)


def _setup_logging() -> None:
    """
    Set up logging using logging.yml if available.

    If 'conf/logging.yml' exists, it will be loaded as a logging configuration.
    Otherwise, default basic logging is set up with INFO level.
    """
    config_path = Path("conf") / "logging.yml"

    if config_path.is_file():
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        )


# Run logging setup automatically at import time
_setup_logging()
