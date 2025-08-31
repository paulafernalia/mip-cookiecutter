import logging
from typing import Dict, Sequence, Tuple

from highspy import Highs

from {{cookiecutter.package_name}}.data.models import ModelData
from {{cookiecutter.package_name}}.optimization.constraints import BaseConstraintBuilder, KnapsackConstraint
from {{cookiecutter.package_name}}.optimization.types import VariableDict
from {{cookiecutter.package_name}}.optimization.variables import BaseVariableBuilder, AssignmentVariable

logger = logging.getLogger(__name__)


class ModelBuilder:
    """Builder for the knapsack optimization model using HiGHS.

    This class encapsulates the creation of decision variables, constraints,
    and the objective function for the knapsack problem. It provides a
    structured pipeline to transform input data into a HiGHS model instance.
    """

    def __init__(self, data: ModelData) -> None:
        """Initialize the model builder.

        Parameters
        ----------
        data : KnapsackData
            The knapsack problem data containing item information and capacity.
        """
        self.data: ModelData = data
        self.model: Highs = Highs()
        self.variables: Dict[str, VariableDict] = {}

        logger.info(f"Initialized KnapsackModelBuilder with ${len(data.items)} items.")

    def _variable_collection(self) -> Sequence[BaseVariableBuilder]:
        """Return the collection of variable builders for the problem.

        Returns
        -------
        Sequence[BaseVariableBuilder]
            A sequence of variable builder instances responsible for creating
            model variables (e.g., assignment variables).
        """
        return [
            AssignmentVariable()
        ]

    def _constraint_collection(self) -> Sequence[BaseConstraintBuilder]:
        """Return the collection of constraint builders for the problem.

        Returns
        -------
        Sequence[BaseConstraintBuilder]
            A sequence of constraint builder instances responsible for creating
            model constraints (e.g., capacity constraints).
        """
        return [
            KnapsackConstraint()
        ]

    def _add_variables(self) -> None:
        """Add decision variables to the model.

        Calls each variable builder from `_variable_collection`, adds the
        variables to the HiGHS model, and stores them in `self.variables`.

        Notes
        -----
        Variables are stored in a nested dictionary where the top-level key is
        the builder name, and the values are mappings from index tuples to HiGHS
        variable references.
        """
        logger.info("Adding decision variables to the model...")
        for creator in self._variable_collection():
            new_variables: VariableDict = creator.add(self.model, self.data)
            # Merge new variables into self.variables, keyed by creator name
            self.variables[creator.name] = new_variables

    def _add_constraints(self) -> None:
        logger.info("Adding constraints to the model...")
        """Add constraints to the model.

        Calls each constraint builder from `_constraint_collection` and
        applies constraints directly to the HiGHS model using the available
        variables and problem data.
        """
        for creator in self._constraint_collection():
            creator.add(self.model, self.data, self.variables)

    def _add_objective(self) -> None:
        """Add the objective function to the optimization model.

        Notes
        -----
        This method must be implemented to define the objective
        (e.g., maximize total value in the knapsack).
        """
        # TODO: implement objective definition here or remove this function
        # logger.info("Defining the objective function...")
        pass

    def build(self) -> Tuple[Highs, Dict[str, VariableDict]]:
        """Build the complete knapsack optimization model.

        This method orchestrates the construction of the model by:
        1. Adding variables
        2. Adding constraints
        3. Defining the objective function

        Returns
        -------
        tuple
            A tuple containing:
            - Highs: The fully constructed HiGHS model instance.
            - VariableDict: Dictionary of model variables keyed by builder name.
        """
        logger.info("Starting to build the knapsack optimization model...")
        self._add_variables()
        self._add_constraints()
        self._add_objective()
        logger.info("Knapsack optimization model successfully built.")

        return self.model, self.variables
