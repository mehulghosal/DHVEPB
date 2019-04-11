import os, time, Data, cv2
import dataProcessing as dp
import numpy as np
import matplotlib.pyplot as plt

directory = os.getcwd() + "/out/"

def main():
	files = dp.sortFiles(dp.initFiles(directory))

	# list of data objects
	data, dataMap = (read(files[2]))
	# newMap = mapRange(dataMap)

	# x = AAAAAAAA(newMap)
	# for i in files:
	# 	d, dm = read(i)
	# 	nm = mapRange(dm)
	# 	x = findCorners(nm)

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

#takes in dataMap and makes a heatMap
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

	img = dataMap
	gray = dataMap

	# img = cv2.imread("test.png")
	# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,2,3,0.04)

	# Threshold for an optimal value, it may vary depending on the image.
	img[dst>0.01*dst.max()]=[255]

	display(img)

#this is the subpixel accuracy thing
def AAAAAAAA(dataMap):
	img = dataMap
	gray = img
	# find Harris corners
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,2,3,0.04)
	dst = cv2.dilate(dst,None)
	ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
	dst = np.uint8(dst)

	# find centroids
	ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

	# define the criteria to stop and refine the corners
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
	corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

	print(len(corners))
	# Now draw them
	res = np.hstack((centroids,corners))
	res = np.int0(res)
	img[res[:,1],res[:,0]]=[255]
	img[res[:,3],res[:,2]] = [255]
	display(img)
	return corners

def display(img, name="img"):
	cv2.imshow(name, img)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()

if __name__ == "__main__":
	main()