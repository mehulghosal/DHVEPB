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
# TODO: RETHINK THIS 
def calc_inst_vel(vectors):
	if not len(vectors)%2: vectors = vectors[:-1] # if odd: take out last frame to get even number

	l = len()
	inst_vels = np.empty((l, 2))

	for i in range(0, len(vectors)-1, 2):
		x1 = vectors[i]
		x2 = vectors[i+1]
		if not(x1.all() and x2.all()): continue
		delta = (np.linalg.norm(x2-x1)) # converting from .2 deg -> meters
		inst_vels.append(delta/180) #converting 3 mins -> seconds
	open("inst_vel.txt", "w").write(np.array(inst_vels))
	return np.array(inst_vels) #in m/s

# vectors.shape = (numcorners, numframes, 2)
# returns avg vels as mag, angle
def calc_avg_vel(vectors):
	l = len(vectors)
	avg_vels = np.empty((l, 2))

	for i in range(l):
		a = vectors[i]
		x = np.delete(a[:,1], np.where(a[:,1] == 0))
		y = np.delete(a[:,0], np.where(a[:,0] == 0))
		dx = x[len(x)-1] - x[0]
		dy = x[len(y)-1] - x[0]
		avg_vels[i, 0] = np.linalg.norm([dx, dy])/len(vectors[0])
		avg_vels[i, 1] = np.degrees(np.arctan([dx, dy]))[0]

	open("avg_vel.txt", "w").write(str(avg_vels))
	return avg_vels

# project the instantaneous vectors onto the average vector
def project():
	pass


def graph_avgs(V):
	origin = [0], [0]
	plt.quiver(*origin, V[:,0], V[:,1], scale=.0005)
	plt.show()


if __name__ == '__main__':
	
	files = sortFiles(initFiles('./out/'), start=0, end=3, r=False)[-110:] #only first 110 frames
	imgs = []
	for i in range(len(files)): 
		imgs.append(read(files[i], crop=False)[1])
		# display(imgs[i], t=30)

	# vectors is list of frames containing the points in the vectors
	# tracks is a list of points tracked
	vectors, tracks = sparse(imgs)
	avg_vels = calc_avg_vel(tracks)
	graph_avgs(avg_vels)
