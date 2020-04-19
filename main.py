import random
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Person(object):
    def __init__(self,x_,y_,id_,infected_):
        self.x=x_
        self.y=y_
        self.id=id_
        self.infected=infected_

# 2D array 
rows, cols = (10, 10) 
grid = [[0 for i in range(cols)] for j in range(rows)] 
#print(grid)

people=[]
for i in range(20):
    tempx = 0
    tempy = 0
    while True:
        tempx = random.randrange(0,10)
        tempy = random.randrange(0,10)
        if grid[tempx][tempy] == 0:
            break
    
    people.append(Person(tempx,tempy,i,False))
    grid[tempx][tempy] = people[i]
        
for p in people:
    plt.plot(p.x, p.y, marker='o', markersize=10    , color="red")

plt.xticks(range(0, 9))
plt.yticks(range(0, 9))

plt.grid()
plt.show()

"""
im = plt.imshow(np.reshape(np.random.rand(100), newshape=(10,10)),
                    interpolation='none', vmin=0, vmax=1, aspect='equal')
ax = plt.gca()
ax.set_xticks(np.arange(0, 10, 1))
ax.set_yticks(np.arange(0, 10, 1))
ax.set_xticklabels(np.arange(1, 11, 1))
ax.set_yticklabels(np.arange(1, 11, 1))
plt.show()"""

"""foo = np.random.rand(35).reshape(5, 7)
# This keeps the default orientation (origin at top left):
extent = (0, foo.shape[1], foo.shape[0], 0)
_, ax = plt.subplots()
ax.imshow(foo, extent=extent)
ax.grid(color='w', linewidth=2)
ax.set_frame_on(False)
plt.show()"""
