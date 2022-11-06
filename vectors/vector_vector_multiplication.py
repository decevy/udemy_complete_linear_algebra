import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = np.array([1,  2, 3,  4, 5, 6])
v2 = np.array([0, -4, 9, -3, 6, 5])

# method 1
dp1 = sum(np.multiply(v1,v2))

# method 1.5
dp15 = sum(v1*v2)

# method 2
dp2 = np.dot(v1,v2) 

# method 3
dp3 = np.matmul(v1,v2)

#method 4
dp4 = 0
for i in range(0, len(v1)):
    dp4 += v1[i]*v2[i]

print(dp1, dp15, dp2, dp3, dp4)