import os, time, Data
import dataProcessing as dp

directory = os.getcwd() + "/output/out"

#file numbers
#returns two file objects
def openFiles(x, y):
	return open(directory + str(x) + ".txt"), open(directory + str(y) + ".txt")

#reads data of one output file
#return map from that file
def read(file):
	inp = file.read().split("\n")[:-1]
	data = []
	for line in inp:
		splitLine = line.split(",")
		data.append(Data.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))
	return data

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data):
	m = [[0 for j in range(501)] for i in range(551)]
	for i in range(len(data)):
		d = data[i]
		m[d.lat][d.lon] = d
	return m

#finds all values < 0
def findNegatives(data):
	negatives = []
	for i in data:
		if i.val < 0:
			negatives.append(i)
	return negatives

#f1 and f2 are maps (returned from formatMap()) of all Data points in a file
#returns map of change in values at each lat, lon
def deltaVals(f1, f2):
	#initializes 2d list 
	m = f1
	for i in range(551):
		for j in range(501):
			d1 = f1[i][j]
			d2 = f2[i][j]
			if d1 == 0 and d2 == 0:
				pass
			elif d1 == 0:
				m[i][j] = d2
			elif d2 ==0:
				m[i][j] = d1
			else:
				m[i][j] = d1 + d2

	return m

def writeMap(m, name):
	f = open(str(name), "w")
	s = ""
	for i in m:
		for j in i:
			s += str(j) + " "
		s += "\n"
	f.write(s)
	f.close()


if __name__ == "__main__":
	files = dp.initFiles(directory)
	files = dp.sortFiles(files)

	f1 = read(open(directory + "1.txt", "r"))
	print(len(findNegatives(f1)))
