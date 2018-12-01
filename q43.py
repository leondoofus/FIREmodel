from data43 import *
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import random


tab = []
for i in range(0,500):
    tab.append(data[i])
fig, ax = plt.subplots()
# Make data.
X = np.arange(0, 500, 1)
Z = np.array(tab)
hmean = np.mean(Z)
fit = stats.norm.pdf(sorted(Z), np.mean(Z), np.std(Z))
ax.bar(X, Z)
ax.plot(Z,fit,'-o')
ax.set_xlim([0,500])
ax.set_ylim([-10,10])
ax.set(xlabel='Consummer', ylabel='UG',
       title='Average UG distribution')

ax.grid()
plt.show()
