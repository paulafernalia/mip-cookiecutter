"""
Base class for optimization model constraints.

This module defines the abstract interface for constraints that can be
applied to an optimization model. Each constraint implementation is
responsible for modifying the solver model based on problem-specific data.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional

from highspy import Highs

from {{cookiecutter.package_name}}.data.models import ModelData
from {{cookiecutter.package_name}}.optimization.base.types import Indices, VariableDict


class BaseConstraintBuilder(ABC):
    """Abstract base class for all optimization constraints."""

    def __init__(self, name: str) -> None:
        """
        Initialize a constraint creator with a unique name.

        Parameters
        ----------
        name : str
            The name of the constraint set.
        """
        self.name = name

    @abstractmethod
    def add(
        self,
        model: Highs,
        data: ModelData,
        variables: Dict[str, VariableDict],
    ) -> None:
        """
        Add a family of constraints to the model using problem data and variable sets.

        Parameters
        ----------
        model : ModelT
            The solver-specific model object.
        data : DataT
            Problem-specific input data.
        **variables : Dict[str, Dict[Tuple[int, ...], highs_var]]
            Arbitrary number of variable sets, keyed by variable set name.
            Each value is a dict mapping index tuples to solver variables.
        """
        raise NotImplementedError

    def constrname(self, index: Optional[Indices] = None) -> str:
        """
        Generate a string representation of a constraint including its name and index.

        Parameters
        ----------
        index : Tuple[int, ...]
            Index of the constraint (e.g., (i,) or (i,j)).

        Returns
        -------
        str
            A readable string representing the constraint.
        """
        if not index:
            return self.name

        index_str = "_".join(map(str, index))
        return f"{self.name}_{index_str}"
