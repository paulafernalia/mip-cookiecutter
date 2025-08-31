# from typing import Dict

# from highspy import Highs

# from {{cookiecutter.package_name}}.data.models import ModelData
# from {{cookiecutter.package_name}}.optimization.base.constraints import BaseConstraintBuilder
# from {{cookiecutter.package_name}}.optimization.base.types import VariableDict


# class KnapsackConstraint(BaseConstraintBuilder):
#     """Knapsack capacity constraint."""

#     def __init__(self) -> None:
#         super().__init__(name="knapsack")

#     def add(
#         self,
#         model: Highs,
#         data: KnapsackData,
#         variables: Dict[str, VariableDict],
#     ) -> None:
#         """
#         Add the knapsack capacity constraint.

#         sum(weights[i] * x[i]) <= capacity.

#         Parameters
#         ----------
#         model : Highs
#             The solver model to which the constraint is added.
#         data : KnapsackData
#             Problem input data.
#         variables : Dict[str, Dict[Tuple[int, ...], highs_var]]
#             Variable sets created by BaseVariable.add, keyed by name.
#         """
#         assignment = variables["assignment"]

#         model.addConstr(
#             expr=model.qsum(
#                 item.weight * assignment[(i,)] for i, item in enumerate(data.items)
#             )
#             <= data.capacity,
#             name=self.constrname(),
#         )
