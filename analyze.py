import os, time, Data
import dataProcessing as dp

directory = "/home/mehulghosal/code/sciresearch/output/"
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

#return a map - see readme at 11/29
def createmap():
	m = [[0 for i in range(501)] for i in range(551)]

if __name__ == "__main__":
	files = dp.initFiles(directory)
	files = dp.sortFiles(files)
	# readFirstFile()
	readOutputs(files)

	dp.closeFiles(files)

