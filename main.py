import os, time, Data, cv2
import dataProcessing as dp
import numpy as np
import matplotlib.pyplot as plt
from optical_flow import flow

directory = os.getcwd() + "/out/"

#reads data of one output file
#return list of data objects and 2d list of values
def read(file):
	file = open(directory+file, "r")
	inp = file.read().split("\n")[:-1]
	data = []
	for line in inp:
		data.append(Data.Data.fromStr(line))

	dataArray = np.array(data)
	dataMap = formatMap(dataArray)

	return dataArray, dataMap

# takes in a dataMap and saves it as a cv2 image
def saveAsImage(img, name):
	cv2.imwrite(directory[:-1] + "imgs/img" + str(name) + ".png",img)

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data):
	m = np.empty([551, 501], float)
	for d in data:
		m[d.lat-1][d.lon-1] = abs(d.val) * 2550
		# m[d.lat-1][d.lon-1][1] = abs(d.val)
		# m[d.lat-1][d.lon-1][2] = abs(d.val)
	return m

def display(img, name="img"):
	cv2.imshow(name, img)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()

if __name__ == "__main__":

	# just list of file names
	files = dp.sortFiles(dp.initFiles(directory))

	# list of data objects
	data, dataMap = (read(files[0]))

	imgs = []
	for i in range(60): 
		imgs.append(read(files[i])[1])

	flow(imgs)