import math
def Readpoints(file_name="18042_det_0.pts"):
	import numpy as np

	link="/home/luffy/Dataset/data/ofdir/"+file_name
	file= open(link)
	dataset = file.readlines()
	file.close()
	strdataset= str(dataset)
	stringdata = strdataset.split(',')

	#print type(stringdata)

	# 3 to 70 as indexed in stringdata
	#print (stringdata[70])
	datapoints=[]
	for i in range(68):
		j=i+3
		datapoints.append(stringdata[j])

	#print(datapoints[0])
	for i in range(len(datapoints)):
		datapoints[i]=datapoints[i].replace("'", "")
		datapoints[i]=datapoints[i][:-2]

	#print datapoints[0]

	points = np.zeros((68,2))#initialise
	#print len(datapoints)
	for i in range(len(datapoints)):
		dummy=[]
		dummy=datapoints[i].split()
		dummy=map(float, dummy)
		points[i][0]=dummy[0]
		points[i][1]=dummy[1]
		del dummy

	#print (points[0][1])
	#print (points[0][1]-1)
	#Normalization
	maxval=np.amax(points,axis=0)
	minval=np.amin(points,axis=0)

	points=points/(maxval-minval)
	#Normalized data
	#print points[1]

	distance=np.zeros(2278) # this is the value of 68C2
	count=0
	for i in range(67):
		j=i+1
		while (j<=67):
			diff = points[i]-points[j]
			power_num=np.power(diff,2)
			distance[count]= math.sqrt(np.sum(power_num))
			count = count + 1
			j= j + 1
			del diff,power_num
	#print count
	#print len(distance)
	#print np.sum(distance)
	return points,distance
	#print distance[100:300]

if __name__ == '__main__':
	Readpoints()