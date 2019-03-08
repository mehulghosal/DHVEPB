import os, time, Data
import dataProcessing as dp
import numpy as np
import matplotlib.pyplot as plt

directory = os.getcwd() + "/out/"

def init():
	global directory
	files = dp.initFiles(directory)
	files = dp.sortFiles(files)
	f = []
	for i in files:
		f.append(read(i))
	return np.asarray(f)

#reads data of one output file
#return list of data objects and 2d list of values
def read(file):
	inp = file.read().split("\n")[:-1]
	data = []
	for line in inp:
		data.append(Data.Data.fromStr(line))

	dataArray = np.array(data)
	dataMap = formatMap(dataArray)

	return dataArray, dataMap

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data):
	m = np.empty([551, 501], float)
	for d in data:
		m[d.lat-1][d.lon-1] = d.val
	return m

#takes in dataMap and makes a heatmap
def heatMap(dataMap):
	plt.imshow(dataMap, cmap='hot', interpolation='nearest')
	plt.show()
	
# use harris corner detection
def findCorners(file):
	MAXLAT = 0
	MAXLON = 0

	MINLAT = 551
	MINLON = 501

	TOPLEFT = file[0]
	TOPRIGHT = file[0]
	BOTTOMLEFT = file[0]
	BOTTOMRIGHT = file[0]
	print(TOPLEFT)
	print(TOPRIGHT)
	print(BOTTOMLEFT)
	print(BOTTOMRIGHT)

	for data in file:
		lat = data.lat
		lon = data.lon
		latChangeMax = False
		lonChangeMax = False
		latChangeMin = False
		lonChangeMin = False

		if lat >= MAXLAT:
			MAXLAT = lat
			latChangeMax = True
		elif lat <= MINLAT:
			MINLAT = lat
			latChangeMin = True

		if lon >= MAXLON:
			MAXLON = lon
			lonChangeMax = True
		elif lon <= MINLON:
			MINLON = lon
			lonChangeMin = True

		if latChangeMax:
			if lonChangeMax:
				TOPRIGHT = data
			elif lonChangeMin:
				TOPLEFT = data
		elif latChangeMin:
			if lonChangeMax:
				BOTTOMRIGHT = data
			elif lonChangeMin:
				BOTTOMLEFT = data

	return [TOPLEFT, TOPRIGHT, BOTTOMLEFT, BOTTOMRIGHT]




if __name__ == "__main__":
	files = dp.sortFiles(dp.initFiles(directory))

	# linear list of data objects
	data, dataMap = (read(files[0]))
	heatMap(dataMap)

	# list of 4 corners in f1
	# f1Corners = findCorners(f1)
	# for i in f1Corners: print(i)