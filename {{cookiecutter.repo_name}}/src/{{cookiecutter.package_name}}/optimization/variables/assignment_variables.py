# from highspy import Highs

# from {{cookiecutter.package_name}}.data.models import KnapsackData
# from {{cookiecutter.package_name}}.optimization.base.types import VariableDict
# from {{cookiecutter.package_name}}.optimization.base.variables import BaseVariableBuilder


# class AssignmentVariable(BaseVariableBuilder):
#     """Create binary variables for knapsack items."""

#     def __init__(self) -> None:
#         super().__init__(name="assignment")

#     def add(self, model: Highs, data: KnapsackData) -> VariableDict:
#         """
#         Add binary variables x[i] for each knapsack item.

#         Parameters
#         ----------
#         model : highspy.Highs
#             The HiGHS model to which variables are added.
#         data : KnapsackData
#             Knapsack problem data (weights, values, capacity).

#         Returns
#         -------
#         Dict[Tuple[int, ...], int]
#             Dictionary mapping (i,) -> column index in HiGHS model.
#         """
#         x_vars: VariableDict = {}

#         for i, value in enumerate(data.values):
#             # Add a binary variable with objective coefficient = item value
#             x_vars[(i,)] = model.addBinary(
#                 obj=-float(value),
#                 name=self.varname((i,)),
#             )

#         return x_vars
