import os, time, Data, cv2
import dataProcessing as dp
from dataProcessing import closeFiles
import numpy as np
import matplotlib.pyplot as plt

directory = os.getcwd() + "/out/"

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
	m = np.empty([551, 501, 3], float)
	for d in data:
		m[d.lat-1][d.lon-1][0] = abs(d.val)
		m[d.lat-1][d.lon-1][1] = abs(d.val)
		m[d.lat-1][d.lon-1][2] = abs(d.val)
	return m

#takes in dataMap and makes a heatMap
def heatMap(dataMap):
	plt.imshow(dataMap, cmap='gray', interpolation='nearest')
	plt.show()

# use harris corner detection/Shi-Tomasi Corner Detector
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html
def findCorners(dataMap):

	img = dataMap

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
	corners = np.int0(corners)

	for i in corners:
		x,y = i.ravel()
		cv2.circle(img,(x,y),3,255,-1)

	display(img)

def display(img, name="img"):
	cv2.imshow(name, img)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()

if __name__ == "__main__":

	files = dp.sortFiles(dp.initFiles(directory))

	# list of data objects
	data, dataMap = (read(files[0]))

	display(dataMap)
	gray = cv2.cvtColor(dataMap,cv2.COLOR_BGR2GRAY)
	# findCorners(dataMap)

	# close files
	openfiles = [files[0]]
	closeFiles(openfiles)