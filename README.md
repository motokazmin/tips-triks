# tips-triks

Howto Convert [[1, 2, 3, 4], [5, 6, 7, 8]] to [1, 2, 3, 4, 5, 6, 7, 8]

import functools, operator
functools.reduce(operator.iconcat, [[1, 2, 3, 4], [5, 6, 7, 8]])
