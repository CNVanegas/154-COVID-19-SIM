import random
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

boardSIZE = 10
infectionRadius = 1
steps = 20
deathchance = 10
recoverychance = 90
SocDist = 1
numOfPeople = 20
grid=[]
people=[]
numInfected = 1
numImmune = 0
numDead = 0
numDeadatStep = 0
numRecoveredatStep = 0

class Person(object):
    def __init__(self,x_,y_,id_,infected_):
        self.x=x_
        self.y=y_
        self.id=id_
        self.infected=infected_
        self.immune=False
        self.timeSinceInfection=0
        self.dead=False
        self.resilience = random.randint(1,9)
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
        global numRecoveredatStep
        global numDeadatStep
        if self.infected == True and self.timeSinceInfection == steps:
            self.timeSinceInfection=0
            randnum = random.randrange(100)
            if randnum < livechance:
                self.immune = True
                self.infected = False
                numInfected-=1
                numImmune+=1
                numRecoveredatStep+=1
            else:
                self.infected = False
                self.dead = True
                grid_[self.x][self.y] = 0
                numInfected-=1
                numDead+=1
                numDeadatStep+=1




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
    global numDeadatStep
    global numRecoveredatStep
    grid = []
    people = []
    numInfected = 1
    numImmune = 0
    numDead = 0
    numDeadatStep = 0
    numRecoveredatStep = 0

def runSim(mode,list1,list2,list3 =[],list4=[],list5=[],list6=[],death=0,recovery=0):
    """
    runSim main functionality is running a random simulation of infection
    with certain givens, being population size, grid size, number of infected,
    death chance percent, and recovery chance percent. 

    *Lists 3-6 Only Used 

    mode:     Determines whether running the Basic Simulation for Part A
              Or Other Customized parameters for later parts that may affect infection.
    List 1:   Is the list containing the total average or newly infected at each step
    List 2:   Is the list containing the total average of already infected
    List 3:   List of Lists Average Recovered
    List 4:   List of Lists Average Dead
    List 5:   List of Lists # Average Dead per step of simulation
    List 6:   List of Lists # Average Recovered per step of simulation 
    Death:    Represents percent chance of death from infection
    Recovery: Represents percent change of recovery from infection

    """
    resetVars()
    newInfected=[]
    alreadyInfected=[] 
    newRecovered = []
    newDead = []
    totDead = []
    totRecovered = []
    initSim()
    timestep = 0
    newInfected.append(0)
    alreadyInfected.append(1)
    newRecovered.append(0)
    newDead.append(0)
    totDead.append(0)
    totRecovered.append(0)
     
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
            numRecov = numRecoveredatStep
            newDied = numDead
            for i in people:
                i.liveOrDie(grid,death,recovery)
            numInfect = numInfected

            for i in people:
                i.step(grid)
            for i in people:
                i.updateInfected(grid)
            timestep+=1
            newInfected.append(numInfected-numInfect) #Keeps Track of number infected at each step
            alreadyInfected.append(numInfect)   #Keeps Track of overall currently infected 
            newRecovered.append(numRecoveredatStep-numRecov)  #Keeps track of recovered at each step
            newDead.append(numDead-newDied)     #keeps track of # dead at each step



    #print(timestep)
    list1.append(newInfected)
    list2.append(alreadyInfected)


    if (mode > 1):
        list3.append(numImmune)
        list4.append(numDead)
        list5.append(newDead)
        list6.append(newRecovered)
    """for p in grid:
        for element in p:
            print(element, end=' ')
        print()    
    print()"""
    resetVars()


totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
totalAvgRecover = []
totalAvgDie = []
totDeadPerStep = []
totRecoverPerStep = []

dfRecoveredAvg = pd.DataFrame()
dfAvgDead = pd.DataFrame()
dfDeadPerStep = pd.DataFrame()
dfRecoveredPerStep = pd.DataFrame()

def resetDfs():
    global totalAvgAlreadyInfected
    global totalAvgNewInfected 
    global totalAvgRecover 
    global totalAvgDie 
    global totDeadPerStep 
    global totRecoverPerStep 
    global dfRecoveredAvg 
    global dfAvgDead 
    global dfDeadPerStep 
    global dfRecoveredPerStep 
    totalAvgAlreadyInfected =[] 
    totalAvgNewInfected =[] 
    totalAvgRecover = []
    totalAvgDie = []
    totDeadPerStep = []
    totRecoverPerStep = []
    dfRecoveredAvg = pd.DataFrame()
    dfAvgDead = pd.DataFrame()
    dfDeadPerStep = pd.DataFrame()
    dfRecoveredPerStep = pd.DataFrame()



partAGotInfected = pd.DataFrame()
partAAlreadyInfected = pd.DataFrame()


#----------------------PART A-----------------------

#Simulation 1 Iteration
for i in range(1):
    runSim(1,totalAvgNewInfected,totalAvgAlreadyInfected)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partAGotInfected["Avg 1"] = tempDF2.mean(axis = 0)
partAAlreadyInfected["Avg 1"] = tempDF.mean(axis = 0)

#Simulation 10 Iterations
totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(10):
    runSim(1,totalAvgNewInfected,totalAvgAlreadyInfected)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partAGotInfected["Avg 10"] = tempDF2.mean(axis = 0)
partAAlreadyInfected["Avg 10"] = tempDF.mean(axis = 0)


#Simulation 100 Iterations
totalAvgAlreadyInfected =[] 
totalAvgNewInfected =[] 
for i in range(100):
    runSim(1,totalAvgNewInfected,totalAvgAlreadyInfected)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
partAGotInfected["Avg 100"] = tempDF2.mean(axis = 0)
partAAlreadyInfected["Avg 100"] = tempDF.mean(axis = 0)

#Simulation 1000 Iterations
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



#--------------------------PART B----------------------------
print("Part B")
print()

partBGotInfected = pd.DataFrame()
partBAlreadyInfected = pd.DataFrame()
partBAvgRecovered = pd.DataFrame()
partBAvgDied = pd.DataFrame()
partBAvgDeadStep = pd.DataFrame()
partBAvgRecoveredStep = pd.DataFrame()

for i in range(1):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,totalAvgRecover,totalAvgDie,totDeadPerStep,totRecoverPerStep,deathchance,recoverychance)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
tempDF3 = pd.DataFrame(totalAvgRecover)
tempDF4 = pd.DataFrame(totalAvgDie)
tempDF5 = pd.DataFrame(totDeadPerStep)
tempDF6 = pd.DataFrame(totRecoverPerStep)
partBGotInfected["Avg 1"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 1"] = tempDF.mean(axis = 0)
partBAvgRecovered["Avg 1"] = tempDF3.mean(axis=0)
partBAvgDied["Avg 1"] = tempDF4.mean(axis=0)
partBAvgDeadStep["Avg 1"] = tempDF5.mean(axis=0)
partBAvgRecoveredStep["Avg 1"] = tempDF6.mean(axis=0)

resetDfs()
for i in range(10):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,totalAvgRecover,totalAvgDie,totDeadPerStep,totRecoverPerStep,deathchance,recoverychance)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
tempDF3 = pd.DataFrame(totalAvgRecover)
tempDF4 = pd.DataFrame(totalAvgDie)
tempDF5 = pd.DataFrame(totDeadPerStep)
tempDF6 = pd.DataFrame(totRecoverPerStep)
partBGotInfected["Avg 10"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 10"] = tempDF.mean(axis = 0)
partBAvgRecovered["Avg 10"] = tempDF3.mean(axis=0)
partBAvgDied["Avg 10"] = tempDF4.mean(axis=0)
partBAvgDeadStep["Avg 10"] = tempDF5.mean(axis=0)
partBAvgRecoveredStep["Avg 10"] = tempDF6.mean(axis=0)

resetDfs()
for i in range(100):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,totalAvgRecover,totalAvgDie,totDeadPerStep,totRecoverPerStep,deathchance,recoverychance)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
tempDF3 = pd.DataFrame(totalAvgRecover)
tempDF4 = pd.DataFrame(totalAvgDie)
tempDF5 = pd.DataFrame(totDeadPerStep)
tempDF6 = pd.DataFrame(totRecoverPerStep)
partBGotInfected["Avg 100"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 100"] = tempDF.mean(axis = 0)
partBAvgRecovered["Avg 100"] = tempDF3.mean(axis=0)
partBAvgDied["Avg 100"] = tempDF4.mean(axis=0)
partBAvgDeadStep["Avg 100"] = tempDF5.mean(axis=0)
partBAvgRecoveredStep["Avg 100"] = tempDF6.mean(axis=0)



resetDfs() 
for i in range(1000):
    runSim(2,totalAvgNewInfected,totalAvgAlreadyInfected,totalAvgRecover,totalAvgDie,totDeadPerStep,totRecoverPerStep,deathchance,recoverychance)

tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
tempDF = pd.DataFrame(totalAvgAlreadyInfected)
tempDF2 = pd.DataFrame(totalAvgNewInfected)
tempDF3 = pd.DataFrame(totalAvgRecover)
tempDF4 = pd.DataFrame(totalAvgDie)
tempDF5 = pd.DataFrame(totDeadPerStep)
tempDF6 = pd.DataFrame(totRecoverPerStep)
partBGotInfected["Avg 1000"] = tempDF2.mean(axis = 0)
partBAlreadyInfected["Avg 1000"] = tempDF.mean(axis = 0)
partBAvgRecovered["Avg 1000"] = tempDF3.mean(axis=0)
partBAvgDied["Avg 1000"] = tempDF4.mean(axis=0)
partBAvgDeadStep["Avg 1000"] = tempDF5.mean(axis=0)
partBAvgRecoveredStep["Avg 1000"] = tempDF6.mean(axis=0)

#tempDF = pd.DataFrame()

#print("Got Infected")
print(partBGotInfected)


#print("Already Infected")
print()
#print(partBAlreadyInfected)

#Need to fix dataframe or redo AvgDied and AvgRecovered since graph formatting off

ax = plt.gca()
plt.title('Average Total Infected Per Step')
plt.xlabel('Steps')
plt.ylabel('# Average Per Step')
partBAlreadyInfected.plot(kind='line',y='Avg 1',color = 'red',ax=ax)
partBAlreadyInfected.plot(kind='line',y='Avg 10',color = 'blue',ax=ax)
partBAlreadyInfected.plot(kind='line',y='Avg 100',color = 'green',ax=ax)
partBAlreadyInfected.plot(kind='line',y='Avg 1000',color = 'purple',ax=ax)
plt.show()

ax = plt.gca()
plt.title('Average Persons Newly Infected Per Step')
plt.xlabel('Steps')
plt.ylabel('# Average Per Step')
partBGotInfected.plot(kind='line',y='Avg 1',color = 'red', ax = ax)
partBGotInfected.plot(kind ='line',y='Avg 10',color = 'blue',ax = ax)
partBGotInfected.plot(kind='line',y='Avg 100', color='green',ax = ax)
partBGotInfected.plot(kind='line',y='Avg 1000',color = 'purple',ax = ax)
plt.show()

ax = plt.gca()
print(partBAvgRecovered)
plt.title('Average Persons Recovered Per Step')
plt.xlabel('Steps')
plt.ylabel('# Average Per Step')
partBAvgRecoveredStep.plot(kind='line',y='Avg 1',color = 'red',ax=ax)
partBAvgRecoveredStep.plot(kind='line',y='Avg 10',color = 'blue',ax=ax)
partBAvgRecoveredStep.plot(kind='line',y='Avg 100',color = 'green',ax=ax)
partBAvgRecoveredStep.plot(kind='line',y='Avg 1000',color = 'purple',ax=ax)
plt.show()

ax = plt.gca()
plt.title('Average Persons Died Per Step')
plt.xlabel('Steps')
plt.ylabel('# Average Per Step')
partBAvgDeadStep.plot(kind='line',y='Avg 1',color = 'red',ax=ax)
partBAvgDeadStep.plot(kind='line',y='Avg 10',color = 'blue',ax=ax)
partBAvgDeadStep.plot(kind='line',y='Avg 100',color = 'green',ax=ax)
partBAvgDeadStep.plot(kind='line',y='Avg 1000',color = 'purple',ax=ax)
plt.show()