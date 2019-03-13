import os, time, Data, cv2
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
	plt.imshow(dataMap, cmap='gray', interpolation='nearest')
	plt.show()
		
# map values to be between 0-255 for colors
# return number between 0-255
def mapRange(dataMap):
	new = np.empty([551, 501], float)
	for row in range(len(dataMap)):
		for i in range(len(dataMap[0])):
			new[row][i] = abs(dataMap[row][i])
	return new

# use harris corner detection/Shi-Tomasi Corner Detector
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html
def findCorners(dataMap):
	# gray = cv2.cvtColor(dataMap,cv2.COLOR_BGR2GRAY)
	# gray = np.float32(gray)
	dst = cv2.cornerHarris(dataMap,2,3,0.04) #what do these numbers mean? we may never know
	# Threshold for an optimal value, it may vary depending on the image.
	img[dataMap>0.01*dst.max()] = [0,0,255]
	cv2.imshow('dst',dataMap)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()

if __name__ == "__main__":
	files = dp.sortFiles(dp.initFiles(directory))

	# linear list of data objects
	data, dataMap = (read(files[0]))
	newMap = mapRange(dataMap)
	
	cv2.imshow('dataMap',dataMap)
	cv2.imshow("newMap", newMap)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()


