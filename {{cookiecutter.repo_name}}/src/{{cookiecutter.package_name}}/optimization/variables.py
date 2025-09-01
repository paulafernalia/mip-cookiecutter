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

# TODO: Implement variables from BaseVariableBuilder
