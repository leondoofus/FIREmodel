from data41 import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig, ax = plt.subplots()

# Make data.
X = np.arange(0, 201, 1)
Z = np.array(data)
Nc = 50
for i in data:
    ax.plot(X, i, label='Nc ='+str(Nc))
    Nc += 50
    ax.legend()

ax.set_xlim([0,200])
ax.set(xlabel='Ticks', ylabel='UG',
       title='UG in function of Nc')
ax.grid()
plt.show()
