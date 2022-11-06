import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = np.array([0,5,0])

# angle == 0
v2 = np.array([0,8,0])
# 0 <= angle <= 90
v3 = np.array([3,2,5]) 
# angle = 90
v4 = np.array([5,0,3])
# angle = 90 <= angle <= 180
v5 = np.array([-2,3,1])
#angle == 180
v6 = np.array([0,-3,0])

print("|v1*v2| =", np.abs(v1.T.dot(v2)), "||v1||*||v2|| =", np.linalg.norm(v1) * np.linalg.norm(v2))
print("|v1*v3| =", np.abs(v1.T.dot(v3)), "||v1||*||v3|| =", np.linalg.norm(v1) * np.linalg.norm(v3))
print("|v1*v4| =", np.abs(v1.T.dot(v4)), "||v1||*||v4|| =", np.linalg.norm(v1) * np.linalg.norm(v4))
print("|v1*v5| =", np.abs(v1.T.dot(v5)), "||v1||*||v5|| =", np.linalg.norm(v1) * np.linalg.norm(v5))
print("|v1*v6| =", np.abs(v1.T.dot(v6)), "||v1||*||v6|| =", np.linalg.norm(v1) * np.linalg.norm(v6))