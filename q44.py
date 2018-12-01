from data44sd import *
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
# Make data.
X = np.arange(0, 201, 1)
Z = np.array(data)
legends = ["[10,40,5,45]","[0,100,0,0]","[100,0,0,0]",
           "[0,0,50,50]","[0,50,25,25]","[50,50,0,0]"]
k = 0
for i in data:
    ax.plot(X, i, label=legends[k])
    k+=1
    ax.legend()

ax.set_xlim([0,200])
ax.set_ylim([1,5])
ax.set(xlabel='Ticks', ylabel='UG',
       title='Standard-deviation UG in function of [NPG,NPO,NPI,NPB]')
# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 1, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left',bbox_to_anchor=(1, 0.5))
ax.grid()
plt.show()
