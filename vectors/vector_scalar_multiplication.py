import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v = np.array([3, -1])
l = -2.3
w = v*l

plt.plot([0, v[0]], [0, v[1]], 'b', label='v')
plt.plot([0, w[0]], [0, w[1]], 'r', label='w')
plt.axis('square')
axlim = max(abs(np.array(v.tolist()+w.tolist()))) * 1.5
plt.axis((-axlim, axlim, -axlim, axlim))
plt.grid()
plt.show()