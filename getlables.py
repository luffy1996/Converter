import pandas
import numpy as np
def getlables():
	dataset = pandas.read_csv("../fer2013.csv")
	colname=list(dataset)
	print colname
	lables=dataset[colname[0]] 
	#print lables[0]
	return lables 
	#Returns Emotion lables

if __name__ == '__main__':
	getlables()