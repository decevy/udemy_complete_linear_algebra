import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2-dimensional vector
v2 = [3, -2]
print(np.array(v2))
print(np.transpose(v2))

# 3-dimensional vector
v3 = [4, -3, 2]
print(np.array(v3))
print(np.transpose(v3))

# row to column (or vice-versa)
v3t = np.transpose(v3)

# plot the 2d vector 
plt.plot([0, v2[0]], [0, v2[1]])
plt.axis('equal')
plt.plot([-4, 4], [0, 0], 'k--')
plt.plot([-0, 0], [-4, 4], 'k--')
plt.grid()
plt.axis((-4, 4, -4 ,4))

# plot the 3d vector
fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(projection='3d')
ax.plot([0, v3[0]], [0, v3[1]], [0, v3[2]],linewidth=3)
ax.plot([0, 0],[0, 0],[-4, 4],'k--')
ax.plot([0, 0],[-4, 4],[0, 0],'k--')
ax.plot([-4, 4],[0, 0],[0, 0],'k--')
plt.show()
 