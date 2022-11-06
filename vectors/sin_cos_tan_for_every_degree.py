from math import sin, cos, tan
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

for i in range(360):
    print("degrees:{:} \tsin:{:.3f} \tcos:{:.3f} \ttan:{:.3f}".format(i, sin(i), cos(i), tan(i)))

