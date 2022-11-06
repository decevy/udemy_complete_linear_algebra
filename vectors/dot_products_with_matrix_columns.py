#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create 2 4*6 matrices of random numbers
a = np.random.rand(4,6)
b = np.random.rand(4,6)

#%%
# use a for-loop to compute dot products between corresponding columns.
def dot_product(m1, m2):
    if m1.shape != m2.shape:
        raise ValueError("Shapes of m1 and m2 are not the same!")

    dot_product = np.zeros((m1.shape[1]))

    for i in range(dot_product.shape[0]):
        dot_product[i] = np.dot(m1[:,i], m2[:,i])

    return dot_product

print(a.dot(b.T))
print(dot_product(a, b))
# %%
