import logging
from typing import List

from highspy import HighsModelStatus

from {{cookiecutter.package_name}}.data.models import Item, ModelData, Solution
from {{cookiecutter.package_name}}.optimization.model_builder import ModelBuilder
from {{cookiecutter.package_name}}.optimization.parameters import Parameters

logger = logging.getLogger(__name__)


class {{cookiecutter.problem_name}}Solver:
    """Concrete solver for the knapsack problem using HiGHS.

    This solver builds a knapsack model with `KnapsackModelBuilder` and
    provides methods to set parameters, solve the model, and extract the solution.
    """

    def __init__(self, data: ModelData) -> None:
        """Initialise instance of knapsack solver.

        Parameters
        ----------
        data : KnapsackData
            The problem data (items, capacities, etc.) required to build the model.

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
        """Solve the knapsack optimization model."""
        self.model.run()

    def build_solution(self) -> Solution | None:
        """Extract the solution from the solved model.

        Returns
        -------
        Solution or None
            The solution of the knapsack problem, or None if not implemented yet.
        """
        if not self.optimal:
            logger.error("Cannot build solution, model is not optimal.")
            return None

        logger.info("Building solution...")
        assignment = self.variables["assignment"]

        selected_items: List[Item] = []
        total_weight = 0
        total_value = 0

        for indices, var in assignment.items():
            value: float = self.model.vals(var)
            if value > 0.5:
                item = self.data.items[indices[0]]

                selected_items.append(item)
                total_weight += item.weight
                total_value += item.value

        return KnapsackSolution(
            items=selected_items,
            weight=total_weight,
            value=total_value,
        )

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
        self.model.writeModel(file_name)
        """
        if not (file_name.endswith(".lp") or file_name.endswith(".mps")):
            raise ValueError("file_name must end with '.lp' or '.mps'")

        self.model.writeModel(file_name)
