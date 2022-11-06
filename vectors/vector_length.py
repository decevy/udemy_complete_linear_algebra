import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# a vector
v = np.array([1,2,3,4,5,6])

# methods 1-4, just like with the regular dot product, e.g.:
v_length1 = np.sqrt(sum(np.multiply(v,v)))

# methods 5: take the norm
v_length2 = np.linalg.norm(v)

print(v_length1, v_length2)
