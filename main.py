from os import walk
import csv
import numpy as np
from readFile import filename
from readpoints import Readpoints
from getlables import getlables

lables=getlables()

f=filename()
file,filenumber=f[0],f[1]
filenumber = map(int , filenumber)
with open('Values.csv', 'w') as csvfile:
	fieldnames = ['name', 'x_distance','y_distance', 'distances','lable']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	count = 0
	for i in range(len(file)):
		if (i%10==0):
			count = count + 1
			print count

		points,distance= Readpoints(file[i])
		writer.writerow({'name': str(filenumber[i]), 'x_distance' : ' '.join(map(str,points[:,0])), 'y_distance' : ' '.join(map(str,points[:,1])), 'distances' : ' '.join(map(str,distance)), 'lable' : str(lables[filenumber[i]])})



