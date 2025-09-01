import logging
from typing import List

from highspy import HighsModelStatus

from {{cookiecutter.package_name}}.data.models import ModelData, Solution
from {{cookiecutter.package_name}}.optimization.model_builder import ModelBuilder
from {{cookiecutter.package_name}}.optimization.parameters import Parameters

logger = logging.getLogger(__name__)


class Engine:
    """Concrete solver for the problem using HiGHS.

    This solver builds a model with `ModelBuilder` and
    provides methods to set parameters, solve the model, and extract the solution.
    """

    def __init__(self, data: ModelData) -> None:
        """Initialise instance of engine.

        Parameters
        ----------
        data : ModelData
            The problem data required to build the model.

        """
        self.data: ModelData = data
        self.model, self.variables = ModelBuilder(data).build()

    @property
    def optimal(self) -> bool:
        """Check if the current model has reached optimality.

        Returns
        -------
        bool
            True if the model status is optimal, False otherwise.
        """
        return self.model.getModelStatus() == HighsModelStatus.kOptimal  # type: ignore

    def run(self) -> None:
        """Solve the optimization model."""
        self.model.run()

    def build_solution(self) -> Solution | None:
        """Extract the solution from the solved model.

        Returns
        -------
        Solution or None
            The solution of the problem, or None if not implemented yet.
        """
        if not self.optimal:
            logger.error("Cannot build solution, model is not optimal.")
            return None

        logger.info("Building solution...")
        # TODO: Implement method to build solution

    def set_parameters(self, params: Parameters) -> None:
        """Set solver parameters for HiGHS.

        Parameters
        ----------
        params : Parameters
            Container for solver configuration, such as time limit or mip gap.
        """
        self.model.setOptionValue("time_limit", params.time_limit)
        self.model.setOptionValue("mip_rel_gap", params.mip_rel_gap)

        if not params.verbose:
            self.model.silent()

    def write_model(self, file_name: str) -> None:
        """
        Write the current optimization model to a file.

        The output format is determined by the file extension:
        - `.lp`  → LP format
        - `.mps` → MPS format

        Parameters
        ----------
        file_name : str
            Path to the file where the model will be written. Must end with
            `.lp` or `.mps`.

        Raises
        ------
        ValueError
            If `file_name` does not end with `.lp` or `.mps`.
        """
        if not (file_name.endswith(".lp") or file_name.endswith(".mps")):
            raise ValueError("file_name must end with '.lp' or '.mps'")

        self.model.writeModel(file_name)
