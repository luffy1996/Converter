from os import walk
import csv
def filename():
	mypath="/home/luffy/Dataset/data/ofdir"
	file = []
	for (dirpath, dirnames, filenames) in walk(mypath):
		file.extend(filenames)
		break
	#print len(file)
	#for i in file:
		#print i
	#print file[0]
	#print type(file[0])
	''' The following will just return the number instead of number_det_0.pts as stored'''
	filenumber = []
	for i in range(len(file)):
		filenumber.append(file[i][:-10])
	#print filenumber
	#print len(filenumber)
	#print filenumber[10000]
	return file,filenumber

if __name__ == '__main__':
	filename()

'''with open('names.csv', 'w') as csvfile:
	fieldnames = ['name', 'x_distance','y_distance']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'name': 'Baked', 'last_name': 'Beans'})'''
	
