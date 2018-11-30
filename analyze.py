import os, time
import dataProcessing

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
			f.append(dataProcessing.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))
		data.append(f)

def readFirstFile():
	global data
	inp = files[0].read().split("\n")[:-1]
	for line in inp:
		splitLine = line.split(",")
		data.append(dataProcessing.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))

def sortFiles(files):
	newList = []
	for f in files:
		newList.append(str(f).split("'")[1])
	#this is a list of file names as strings
	newList.sort()
	dataProcessing.closeFiles(files)
	files = []
	#re-adds each file into files in alphabetical order
	for fname in newList:
		#fname is in format: "<_io.TextIOWrapper name='newdata/dtec2dmap_11344_epoch467.txt' mode='r' encoding='UTF-8'>"
		#print(fname)
		#name = fname[33:-28] #this splices fname --> "newdata....txt"
		files.append(open(fname, "r"))
	#this should leave files as sorted

	return files


if __name__ == "__main__":
	files = dataProcessing.initFiles(directory)
	files = sortFiles(files)
	# readFirstFile()
	readOutputs(files)

	dataProcessing.closeFiles(files)

