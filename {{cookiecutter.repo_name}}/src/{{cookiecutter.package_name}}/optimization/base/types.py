from typing import Dict, Tuple

from highspy.highs import highs_var

# Type alias for variable dictionaries keyed by index tuples
Indices = Tuple[int, ...]
VariableDict = Dict[Indices, highs_var]
