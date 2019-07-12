import os, time, Data, cv2
import numpy as np
import matplotlib.pyplot as plt
from optical_flow import flow
from dataProcessing import *
from img_reg import *

#reads data of one output file
#return list of data objects and 2d list of values
def read(file):
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
	dataMap = formatMap(dataArray)

	return dataArray, dataMap

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data):
	m = np.empty([551, 501, 3], dtype=np.uint8)
	for d in data:
		if abs(d.val)>50: 
			d.set_val(0)
		mult = 30
		m[551-(d.lat+1)][d.lon-1][0] = abs(d.val) * mult
		m[551-(d.lat+1)][d.lon-1][1] = abs(d.val) * mult
		m[551-(d.lat+1)][d.lon-1][2] = abs(d.val) * mult
	return m

if __name__ == '__main__':
	
	# just list of file names
	files = sortFiles(initFiles('./out/'), start=0, end=3)
	imgs = []
	for i in range(10): 
		imgs.append(read(files[i])[1])

	first_frame, last_frame, overlay = flow(imgs)
	
	display(first_frame, name="first frame")
	display(last_frame, name="last frame")
	display(overlay, name="overlay")
