import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# generate two 100-element random row vectors,
rows = 100
a = np.random.randn(rows)
b = np.random.randn(rows)
# compute dot product a with b, b with a
print("a'*b", a.T.dot(b))
print("b'*a", b.T.dot(a))

# generate two 2-element random row vectors,
rows = 2
a = np.random.randn(rows)
b = np.random.randn(rows)
# compute dot product a with b, b with a
print("a'*b", a.T.dot(b))
print("b'*a", b.T.dot(a))
