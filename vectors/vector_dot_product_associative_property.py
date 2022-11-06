import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create random vectors
n = 5
a = np.random.rand(n)
b = np.random.rand(n)
c = np.random.rand(n)

# the two results
res1 = a.dot(b.dot(c))
res2 = np.array(a.dot(b)).dot(c)

# print them
print(res1)
print(res2)

### special cases where associative property works!
# 1) one vector is the zeros vector
# 2) a==b==c
# 2) a(b*c) where a==c
# 3) a(b*c) where a==-c