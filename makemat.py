import pandas
import numpy as np
import scipy.misc
dataset = pandas.read_csv("fer2013.csv")
print (dataset.shape)
print(list(dataset))
colname=list(dataset)
print colname[1]
picset = dataset[colname[1]]
print(picset.shape)
#print picset[1:10]
#print type(picset[0])
#A=picset[2].split()
#print type(A)
#A = map(int,A)
#A = np.asarray(A)
#print type(A)
#A=np.reshape(A,(48,48))
#print A.shape
print 48*48
#print picset[0].shape

for i in range(picset.shape[0]):
	a=[]
	a=picset[i].split()
	a=map(int,a)
	a=np.asarray(a)
	a=np.reshape(a,(48,48))
	foldernum=int(i/10000)
	name="data"+str(foldernum)+"/"+str(i)+".jpg"
	scipy.misc.imsave(name, a)
	#print type(a)
print "ho gaya"
