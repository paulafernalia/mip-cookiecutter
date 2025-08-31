"""
Base interface for defining decision variables in optimization models.

This module provides an abstract base class ``BaseVariable`` that follows the
Composite pattern for adding variables to solver models. Subclasses should
implement the ``add`` method to define specific decision variables based on
the provided problem data.

Examples
--------
A binary variable for item selection in a knapsack problem can be implemented
as a subclass of ``BaseVariable``:

    class ItemSelectionVariable(BaseVariable[KnapsackData, highspy.Highs]):
        def add(self, model: highspy.Highs, data: KnapsackData) -> None:
            # Add binary variables x[i] for each item i
            for i in range(len(data.items)):
                model.addVar(lb=0, ub=1, vtype="B", name=f"x_{i}")

"""

from abc import ABC, abstractmethod

from highspy import Highs

from {{cookiecutter.package_name}}.data.models import ModelData
from {{cookiecutter.package_name}}.optimization.types import Indices, VariableDict


class BaseVariableBuilder(ABC):
    """Abstract base class representing a decision variable in an optimization model."""

    def __init__(self, name: str) -> None:
        """
        Initialize a variable creator with a unique name.

        Parameters
        ----------
        name : str
            The name of the variable set.
        """
        self.name = name

    @abstractmethod
    def add(self, model: Highs, data: ModelData) -> VariableDict:
        """
        Add the variable(s) to the optimization model.

        Parameters
        ----------
        model : ModelT
            The solver-specific optimization model where the variable
            should be defined.
        data : DataT
            The problem-specific input data used to determine the size,
            bounds, or other properties of the variable.

        Returns
        -------
        dict[tuple[int, ...], VarT]
            A mapping from index tuples to solver variables.
        """
        raise NotImplementedError

    def varname(self, index: Indices) -> str:
        """
        Generate a string representation of a variable including its name and index.

        Parameters
        ----------
        index : Tuple[int, ...]
            Index of the variable (e.g., (i,) or (i,j)).

        Returns
        -------
        str
            A readable string representing the variable.
        """
        index_str = "_".join(map(str, index))
        return f"{self.name}_{index_str}"


class AssignmentVariable(BaseVariableBuilder):
    """Create binary variables for knapsack items."""

    def __init__(self) -> None:
        super().__init__(name="assignment")

    def add(self, model: Highs, data: ModelData) -> VariableDict:
        """
        Add binary variables x[i] for each knapsack item.

        Parameters
        ----------
        model : highspy.Highs
            The HiGHS model to which variables are added.
        data : KnapsackData
            Knapsack problem data (weights, values, capacity).

        Returns
        -------
        Dict[Tuple[int, ...], int]
            Dictionary mapping (i,) -> column index in HiGHS model.
        """
        x_vars: VariableDict = {}

        for i, value in enumerate(data.values):
            # Add a binary variable with objective coefficient = item value
            x_vars[(i,)] = model.addBinary(
                obj=-float(value),
                name=self.varname((i,)),
            )

        return x_vars
