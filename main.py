import random
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

boardSIZE = 10
numOfPeople = 20
grid=[]
people=[]
numInfected = 1
numImmune = 0
numDead = 0
class Person(object):
    def __init__(self,x_,y_,id_,infected_):
        self.x=x_
        self.y=y_
        self.id=id_
        self.infected=infected_
        self.immune=False
        self.timeSinceInfection=0
        self.dead=False
    def __str__(self):
        if self.infected == True:
            return "I"
        else:
            return "S"

    def step(self, grid_):
        """
        Purpose is to generate random movement of the people inside grid

        Self used to denote the person object, grid being the map of people positions
        and movements possible
        """
        if self.dead == True:
            return
        if self.infected == True:
            self.timeSinceInfection+=1

        #get direction up down left right and move if it is open.
        # 0 = up 1 = down 2=left 3=right
        dirs = [0,1,2,3]
        random.shuffle(dirs) #Movement directions randomized for random movement
        for i in dirs:
            if i == 0:
                if (self.y-1 > 0) and (grid_[self.x][self.y-1] == 0):
                    grid_[self.x][self.y] = 0   #Current square of person set to 0 after once they've moved
                    self.y -= 1
                    grid_[self.x][self.y] = self #Updating grid to contain person
                    break
            elif i == 1:
                if (self.y+1 < boardSIZE-1) and (grid_[self.x][self.y+1] == 0):
                    grid_[self.x][self.y] = 0 #Current square of person set to 0 after once they've moved
                    self.y += 1
                    grid_[self.x][self.y] = self #Updating grid to contain person
                    break
            elif i == 2:
                if  (self.x-1 > 0) and (grid_[self.x-1][self.y] == 0):
                    grid_[self.x][self.y] = 0 #Current square of person set to 0 after once they've moved
                    self.x -= 1
                    grid_[self.x][self.y] = self #Updating grid to contain person
                    break
            elif i == 3:
                if (self.x+1 < boardSIZE-1) and (grid_[self.x+1][self.y] == 0):
                    grid_[self.x][self.y] = 0 #Current square of person set to 0 after once they've moved
                    self.x += 1
                    grid_[self.x][self.y] = self #Updating grid to contain person
                    break
            #put code for checking virus either here or down below after all people have moved.

    def updateInfected(self, grid_):
        dirs = [0,1,2,3]
        #get direction up down left right and move if it is open.
        # 0 = up 1 = down 2=left 3=right
        global numInfected
        if self.infected == False and self.immune == False and self.dead == False:
            for i in dirs:
                if i == 0:
                    if (self.y-1 > 0) and (grid_[self.x][self.y-1] != 0) and (grid_[self.x][self.y-1].infected == True):
                        self.infected=True
                        numInfected+=1
                        break
                elif i == 1:
                    if (self.y+1 < boardSIZE-1) and (grid_[self.x][self.y+1] != 0) and (grid_[self.x][self.y+1].infected == True):
                        self.infected=True
                        numInfected+=1
                        break
                elif i == 2:
                    if  (self.x-1 > 0) and (grid_[self.x-1][self.y] != 0) and (grid_[self.x-1][self.y].infected == True):
                        self.infected=True
                        numInfected+=1
                        break
                elif i == 3:
                    if (self.x+1 < boardSIZE-1) and (grid_[self.x+1][self.y] != 0) and (grid_[self.x+1][self.y].infected == True):
                        self.infected=True
                        numInfected+=1
                        break

    def liveOrDie(self, grid_,diechance,livechance):
        """
        Function determines whether and infected person in the grid recovers
        or dies from the infection based on predetermined chance percentages 
        """
        global numDead
        global numImmune
        global numInfected
        if self.infected == True and self.timeSinceInfection == 20:
            self.timeSinceInfection=0
            randnum = random.randrange(100)
            if randnum < livechance:
                self.immune = True
                self.infected = False
                numInfected-=1
                numImmune+=1
            else:
                self.infected = False
                self.dead = True
                grid_[self.x][self.y] = 0
                numInfected-=1
                numDead+=1




def initSim():
    # 2D array 
    rows, cols = (boardSIZE, boardSIZE)
    global grid
    global people
    grid = [[0 for i in range(cols)] for j in range(rows)] 
#print(grid)
    for i in range(numOfPeople):
        tempx = 0
        tempy = 0
        while True:
            tempx = random.randrange(0,boardSIZE)
            tempy = random.randrange(0,boardSIZE)
            if grid[tempx][tempy] == 0:
                break
    
        people.append(Person(tempx,tempy,i,False))
        grid[tempx][tempy] = people[i]
    people[random.randrange(0,len(people)-1)].infected = True
    #for p in grid:
        #for element in p:
           #print(element, end=' ')
        #print()

def resetVars():
    global grid
    global people
    global numInfected
    global numImmune
    global numDead
    grid = []
    people = []
    numInfected = 1
    numImmune = 0
    numDead = 0

def runSim(mode,list1,list2,list3=[],death=0,recovery=0):
    """
    runSim main functionality is running a random simulation of infection
    with certain givens, being population size, grid size, number of infected,
    death chance percent, and recovery chance percent. 

    mode: Determines whether running the Basic Simulation for Part A
          Or Other Customized parameters for later parts that may affect infection.
    List 1: Is the list containing the total average or newly infected
    List 2: Is the list containing the total average of already infected
    List 3: Currently Unused
    Death: Represents percent chance of death from infection
    Recovery: Represents percent change of recovery from infection
    
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