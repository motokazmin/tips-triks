# tips-triks

HOWTO Convert [[1, 2, 3, 4], [5, 6, 7, 8]] to [1, 2, 3, 4, 5, 6, 7, 8]

import functools, operator
functools.reduce(operator.iconcat, [[1, 2, 3, 4], [5, 6, 7, 8]])


HOWTO split string list and create new DataFrame:
We have :
	    id  names  
	0   1   ab c
	1   2   s
	2   1   dm ab aaa
We want:
            id  names
	0   1   ab
	1   1   c
	2   2   s
	3   1   dm
	4   1   ab
	5   1   aaa

Solution: df[['id']].join(df['names'].str.split().explode())

HOWTO fast add new elements to DataFrame:
df = []
for i in some:
  df.append({'a' : 1, 'b' : 2})

df = pd.DataFrame(df)


HOWTO import from local directory:
import sys
sys.path.append('your path')
