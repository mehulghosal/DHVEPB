import os, time, Data, pygame
import dataProcessing as dp

directory = str(os.getcwd()) + "/output/"
#this will be a 2d list, each entry will be a file
data = []

def readOutputs(files):
	global data
	for file in files:
		f =[]
		inp = files[0].read().split("\n")[:-1]
		for line in inp:
			splitLine = line.split(",")
			f.append(Data.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))
		data.append(f)


#f1 and f2 are lists of all Data points in a file
#returns map of change in values at each lat, lon
def deltaVals(f1, f2):
	#initializes 2d list 
	m = [[Data.Data((data.index(f1)+data.index(f2))/2, i, j, 0) for j in range(1, 502)] for i in range(1, 552)]
	# print(len(f1))
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
	# readFirstFile()
	readOutputs(files)
	# print(len(data[1]))
	m = calc()
	for i in m:
		draw(initRects(m))

	dp.closeFiles(files)

