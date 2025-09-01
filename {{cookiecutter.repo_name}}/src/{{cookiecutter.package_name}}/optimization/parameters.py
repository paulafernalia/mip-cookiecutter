"""Defines schema of data model used in the problem."""

from pydantic import BaseModel, PositiveFloat, PositiveInt


class Parameters(BaseModel):
    """Pydantic model of high level data model used in this problem."""

    mip_rel_gap: PositiveFloat = 1e-5
    time_limit: PositiveInt = 600
    verbose: bool = False
