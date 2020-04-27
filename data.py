import csv
import random
import time


x_value = 0
total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0
 
days = 100
fieldnames = ["x_value", "total_1", "total_2", "total_3", "total_4"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while x_value <= days:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2,
            "total_3": total_3,
            "total_4": total_4
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2, total_3, total_4)

        x_value += 1
        if (random.randint(0,100) >= 0):	# random 100% chance person can get infected
        	total_1 = total_1 + 1
        if (random.randint(0,100) > 50):    # random 50% chance person can get infected (washes hand + facemask)
            total_2 = total_2 + 1
        if (random.randint(0,100) > 70):    # random 30% chance person can get infected (social distance)
            total_3 = total_3 + 1
        if (random.randint(0,100) > 95):    # random 5% chance person can get infected (social distance)
            total_4 = total_4 + 1
       

    time.sleep(.500)		# sleep for 1 second before spit out new value, change to millisecon if too long (.500 = half second)