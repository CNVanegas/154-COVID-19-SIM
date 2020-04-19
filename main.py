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
rows, cols = (100, 100) 
grid = [[0 for i in range(cols)] for j in range(rows)] 
#print(grid)

people=[]
for i in range(200):
    people.append(Person(1,1,i,False))
