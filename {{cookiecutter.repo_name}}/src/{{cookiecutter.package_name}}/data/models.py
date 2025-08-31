"""Defines schema of data model used in the problem."""

from typing import List

from pydantic import BaseModel, NonNegativeInt, PositiveInt


class Item(BaseModel):
    """Data model of an item of the knapsack problem."""

    weight: PositiveInt
    value: NonNegativeInt


class ModelData(BaseModel):
    """Problem data model."""

    capacity: PositiveInt
    items: List[Item]

    @property
    def n(self) -> int:
        """Return number of items."""
        return len(self.items)

    @property
    def weights(self) -> List[NonNegativeInt]:
        """Return array of weights."""
        return [item.weight for item in self.items]

    @property
    def values(self) -> List[PositiveInt]:
        """Return array of weights."""
        return [item.value for item in self.items]


class Solution(BaseModel):
    """Solution to the knapsack problem."""

    items: List[Item]
    weight: NonNegativeInt
    value: NonNegativeInt
