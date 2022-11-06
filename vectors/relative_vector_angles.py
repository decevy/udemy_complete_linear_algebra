import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, -2])
b = np.array([2, 3])
c = np.array([0, 2])

print(f"a*b = {a.T.dot(b)}, ||a||*||b|| = {np.linalg.norm(a)*np.linalg.norm(b)}")
print(f"a*c = {a.T.dot(c)}, ||a||*||c|| = {np.linalg.norm(a)*np.linalg.norm(c)}")
print(f"b*c = {b.T.dot(c)}, ||b||*||c|| = {np.linalg.norm(b)*np.linalg.norm(c)}")

plt.plot([0, a[0]], [0, a[1]], 'b', label='a')
plt.plot([0, b[0]], [0, b[1]], 'r', label='b')
plt.plot([0, c[0]], [0, c[1]], 'k', label='c')
plt.legend()
plt.axis('square')
plt.axis((-6, 6, -6, 6))
plt.grid()
plt.show()