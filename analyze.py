import os, time, Data, pygame
import dataProcessing as dp

directory = str(os.getcwd()) + "/output/"

#reads data of one output file
#return map from that file
def read(file):
	inp = file.read().split("\n")[:-1]
	data = []
	for line in inp:
		splitLine = line.split(",")
		data.append(Data.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))
	return formatMap(data)

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data):
	m = [[0 for j in range(501)] for i in range(551)]
	for i in range(len(data)):
		d = data[i]
		m[d.lat][d.lon] = d
	return m

#f1 and f2 are lists of all Data points in a file
#returns map of change in values at each lat, lon
def deltaVals(f1, f2):
	#initializes 2d list 
	m = []
	# for i in range()

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
	


	dp.closeFiles(files)

