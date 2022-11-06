import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = np.array([2,4,-3])
v2 = np.array([0,-3,-3])

angle_v1_v2 = np.arccos( np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2)) )

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], 'b')
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], 'r')

plt.axis((-6,6,-6,6))
plt.title('Angle between vectors: %s rad.' %angle_v1_v2)
plt.show()

dot_product_algebraic = np.dot(v1,v2)
dot_product_geometric = np.linalg.norm(v1) * np.linalg.norm(v2) * np.cos(angle_v1_v2)

print("dot product algebraic:", dot_product_algebraic)
print("dot product geometric", dot_product_geometric)