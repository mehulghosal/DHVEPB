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

	file.close()
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
def crop(m, left=200, top=50, right=500, bottom=400):
	return m[top:bottom, left:right].copy()

# return inst velocities from frame to next
def calc_inst_vel(vectors):
	vectors = vectors[1:] # take out first frame to get even number
	inst_vels = []
	for i in range(0, len(vectors)-1, 2):
		x1 = vectors[i]
		x2 = vectors[i+1]
		delta = (x2-x1)/50 * 110 * 1000 # converting from .2 deg -> meters
		inst_vels.append(delta/180) #converting 3 mins -> seconds
	return np.swapaxes(np.array(inst_vels), 0, 1) #in m/s

# take tracks and return avg velocities
# vectors.shape = (numcorners, numframes, 2)
# returns 1-d array with avg vels of each hobject
def calc_avg_vel(vectors):
	avg_vels = np.zeros(50)

if __name__ == '__main__':
	
	files = sortFiles(initFiles('./out/'), start=0, end=3, r=True)[-110:] #only first 110 frames
	imgs = []
	for i in range(30): 
		imgs.append(read(files[i], crop=False)[1])
		# display(imgs[i], t=30)

	# vectors is list of frames containing the points in the vectors
	# tracks is a list of points tracked
	vectors, tracks = sparse(imgs)
	inst_velocities = calc_inst_vel(vectors)