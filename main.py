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
    def __str__(self):
        if self.infected == True:
            return "I"
        else:
            return "S"



grid=[]
people=[]
def initSim():
    # 2D array 
    rows, cols = (10, 10) 
    grid = [[0 for i in range(cols)] for j in range(rows)] 
#print(grid)
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
    people[random.randrange(0,len(people)-1)].infected = True
    for p in grid:
        for element in p:
            print(element, end=' ')
        print()
initSim()