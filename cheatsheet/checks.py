
a = {1:1, 2:2, 3:"b"}
b = {1:1, 2:2, 3:"b"}
c = a
print("a =", a)
print("b =", b)
print("link(a) c =", c)
print("a == b", a == b)
print("a is b", a is b)
print("a == c", a == c)
print("a is c", a is c)
print("b == c", b == c)
print("b is c", b is c)

import numpy as np
print(len(set([2, 3, 3, np.nan, 7])))

from collections import defaultdict

d = defaultdict(lambda : 0)
d[1] += 1
print(d[1])
