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

    def step(self, grid_):
        dirs = [0,1,2,3]
        random.shuffle(dirs)
        #get direction up down left right and move if it is open.
        # 0 = up 1 = down 2=left 3=right
        for i in dirs:
            if i == 0:
                if grid_[self.x][self.y-1] == 0:
                    grid_[self.x][self.y] = 0
                    self.y -= 1
                    grid_[self.x][self.y] = self
                    break
            elif i == 1:
                if grid_[self.x][self.y+1] == 0:
                    grid_[self.x][self.y] = 0
                    self.y += 1
                    grid_[self.x][self.y] = self
                    break
            elif i == 2:
                if grid_[self.x-1][self.y] == 0:
                    grid_[self.x][self.y] = 0
                    self.x -= 1
                    grid_[self.x][self.y] = self
                    break
            elif i == 3:
                if grid_[self.x+1][self.y] == 0:
                    grid_[self.x][self.y] = 0
                    self.x += 1
                    grid_[self.x][self.y] = self
                    break
            #put code for checking virus either here or down below after all people have moved.

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