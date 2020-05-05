import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use("seaborn")

index = count()


def animate(i):
	data = pd.read_csv("data.csv") # read data from csv generator
	x = data["x_value"]				# assign data for x (days)
	y1 = data["total_1"]				# assign data for y (cases)
	y2 = data["total_2"]
	y3 = data["total_3"]
	y4 = data["total_4"]
	plt.cla()						# clear out the old frame before drawing new frame
	plt.plot(x,y1, color="blue", label = "100% Chance Infection (Do nothing)")					# draw value of x (days) and y (case)
	plt.plot(x,y2, color="red", label = "50% Chance Infection (Intervention)")
	plt.plot(x,y3, color="green", label = "30% Chance Infection (Social Distance)")
	plt.plot(x,y4, color="purple", label = "5% Chance Infection (Social Distance + Intervention)")
	plt.xlabel ("Days")				# label for x axis
	plt.ylabel("Cases")				# label for y axis	
	plt.title("CCP Virus SIM")		# title of the thing
	plt.tight_layout()				# idk what this does

	plt.legend()
#xx = [1, 2, 3]
#yy = [4, 5, 6]
#plot3 = plt.figure(3)
#plt.plot(xx,yy)
ani = FuncAnimation(plt.gcf(), animate, interval = 500) # gcf = get current figure, interval = how fast to draw (in millisecond)
plt.tight_layout()
plt.show()			# Draw everything on the screen
