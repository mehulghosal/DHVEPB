import os, time, Data, cv2
import numpy as np
import matplotlib.pyplot as plt
from optical_flow import *
from dataProcessing import *

#reads data of one output file
#return list of data objects and 2d list of values
def read(file, crop=False):
	file = open('./out/'+file, "r")
	print(file)
	inp = file.read().split("\n")
	data = []
	for line in inp:
		spl = line.split()
		if len(spl)==0: continue
		for d in spl:
			data.append(Data.Data.fromStr(d))
	dataArray = np.array(data)
	dataMap = formatMap(dataArray, cr=crop)

	return dataArray, dataMap

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data, cr=False):
	m = np.empty([551, 501, 3], dtype=np.float64)
	for d in data:
		if abs(d.val)>50: 
			d.set_val(0)
		mult = 35
		for i in range(3):
			m[501-d.lat-1][d.lon-1][i] = abs(d.val) * mult
	if cr: return crop(m)
	m = cv2.threshold(m.astype(np.uint8),40,255,cv2.THRESH_TOZERO)[1]
	return m

# top bound: 200,90
# bottom: 500,400
def crop(m, left=200, top=80, right=500, bottom=400):
	return m[top:bottom, left:right]

if __name__ == '__main__':
	
	# just list of file names
	files = sortFiles(initFiles('./out/'), start=0, end=3, r=True)
	imgs = []
	for i in range(len(files)): 
		imgs.append(read(files[i], crop=False)[1])
		# display(imgs[i], t=100)

	# first_frame, last_frame, overlay = flow(imgs)
	
	# display(first_frame, name="first frame")
	# display(last_frame, name="last frame")
	# display(overlay, name="overlay")

	sparse(imgs)