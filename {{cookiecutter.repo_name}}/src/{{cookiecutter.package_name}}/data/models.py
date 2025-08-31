from typing import List

from pydantic import BaseModel, NonNegativeInt, PositiveInt


class Item(BaseModel):
    """
    Data model representing an item in the knapsack problem.

    Attributes:
        weight (PositiveInt): Weight of the item. Must be a positive integer.
        value (NonNegativeInt): Value of the item. Must be a non-negative integer.
    """

    weight: PositiveInt
    value: NonNegativeInt


class ModelData(BaseModel):
    """
    Data model for a knapsack problem instance.

    Attributes:
        capacity (PositiveInt): Maximum weight capacity of the knapsack.
        items (List[Item]): List of items available to include in the knapsack.

    Properties:
        n (int): Number of items in the list.
        weights (List[NonNegativeInt]): List of weights of all items.
        values (List[PositiveInt]): List of values of all items.
    """

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
    """
    Represents a solution to the knapsack problem.

    Attributes:
        items (List[Item]): List of items included in the solution.
        weight (NonNegativeInt): Total weight of the selected items.
        value (NonNegativeInt): Total value of the selected items.
    """

    items: List[Item]
    weight: NonNegativeInt
    value: NonNegativeInt
