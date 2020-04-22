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
    
<<<<<<< Updated upstream
    people.append(Person(tempx,tempy,i,False))
    grid[tempx][tempy] = people[i]
        
for p in people:
    plt.plot(p.x, p.y, marker='o', markersize=10    , color="red")

plt.xticks(range(0, 11))
plt.yticks(range(0, 11))

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
=======
    """
    resetVars()
    newInfected=[]
    alreadyInfected=[] 
    initSim()
    timestep = 0
    newInfected.append(0)
    alreadyInfected.append(1)
     
     #mode1 is part A, else is other modes for now
    if mode == 1:
        while numInfected < numOfPeople:
            numInfect = numInfected
            for i in people:
                i.step(grid)
            for i in people:
                i.updateInfected(grid)
            timestep+=1
            newInfected.append(numInfected-numInfect)
            alreadyInfected.append(numInfect)
    else:
        while numInfected > 0:
            for i in people:
                i.liveOrDie(grid,death,recovery)
            numInfect = numInfected

            for i in people:
                i.step(grid)
            for i in people:
                i.updateInfected(grid)
            timestep+=1
            newInfected.append(numInfected-numInfect)
            alreadyInfected.append(numInfect)

    #print(timestep)
    list2.append(alreadyInfected)
    list1.append(newInfected)
    """for p in grid:
        for element in p:
            print(element, end=' ')
        print()    
    print()"""
    resetVars()
totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
partAGotInfected = pd.DataFrame()
partAAlreadyInfected = pd.DataFrame()


#PART A
for i in range(1):
    runSim(1,totalAvgNewInfected,totalAvgAlreadyInfected)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partAGotInfected["Avg 1"] = tempDF2.mean(axis = 0)
partAAlreadyInfected["Avg 1"] = tempDF.mean(axis = 0)

totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(10):
    runSim(1,totalAvgNewInfected,totalAvgAlreadyInfected)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partAGotInfected["Avg 10"] = tempDF2.mean(axis = 0)
partAAlreadyInfected["Avg 10"] = tempDF.mean(axis = 0)

totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(100):
    runSim(1,totalAvgNewInfected,totalAvgAlreadyInfected)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partAGotInfected["Avg 100"] = tempDF2.mean(axis = 0)
partAAlreadyInfected["Avg 100"] = tempDF.mean(axis = 0)

totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(1000):
    runSim(1,totalAvgNewInfected,totalAvgAlreadyInfected)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partAGotInfected["Avg 1000"] = tempDF2.mean(axis = 0)
partAAlreadyInfected["Avg 1000"] = tempDF.mean(axis = 0)

print(partAGotInfected)
print()
print(partAAlreadyInfected)


#PART B
print()
totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[]
temp =[] 

partBGotInfected = pd.DataFrame()
partBAlreadyInfected = pd.DataFrame()

for i in range(1):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,temp,10,90)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partBGotInfected["Avg 1"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 1"] = tempDF.mean(axis = 0)

totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(10):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,temp,10,90)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partBGotInfected["Avg 10"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 10"] = tempDF.mean(axis = 0)

totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(100):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,temp,10,90)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partBGotInfected["Avg 100"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 100"] = tempDF.mean(axis = 0)

totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(1000):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,temp,10,90)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partBGotInfected["Avg 1000"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 1000"] = tempDF.mean(axis = 0)

print(partBGotInfected)
print()
print(partBAlreadyInfected)
print()
>>>>>>> Stashed changes
