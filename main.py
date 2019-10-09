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
	m = np.zeros([551, 501, 3], dtype=np.float64)
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
# vectors.shape -> 50, 109, 2
def calc_inst_vel(vectors):
	l = vectors.shape
	if not l[1]%2: vectors = vectors[:,:-1,:] # if odd: take out last frame to get even number
	inst_vels = np.zeros((l[0], l[1], 2))
	all_v = []

	for artifact in vectors:
		inst_vel = np.zeros(l[1], 2)

		# ignore last frame bc theres nowhere it goes
		for i in range(len(artifact) - 1):
			pass
		


# vectors.shape = (numcorners, numframes, 2)
# returns avg vels as mag, angle
def calc_avg_vel(vectors):
	l = len(vectors)
	avg_vels = np.zeros((l, 2))

	for i in range(l):
		a = vectors[i]
		x = np.delete(a[:,1], np.where(a[:,1] == 0))
		y = np.delete(a[:,0], np.where(a[:,0] == 0))
		dx = x[len(x)-1] - x[0]
		dy = y[len(y)-1] - y[0]
		avg_vels[i, 0] = dx
		avg_vels[i, 1] = dy
		# avg_vels[i, 0] = np.linalg.norm([dx, dy])/len(vectors[0])
		# avg_vels[i, 1] = np.degrees(np.arctan([dx, dy]))[0]

	open("avg_vel.txt", "w").write(str(avg_vels))
	return avg_vels

# project the instantaneous vectors onto the average vector
def project():
	pass


def graph_avgs(V):
	origin = [0], [0]
	plt.quiver(*origin, V[:,1], V[:,0], units='xy')
	plt.show()


if __name__ == '__main__':
	
	files = sortFiles(initFiles('./out/'), start=0, end=3, r=True)[-110:] #only first 110 frames
	imgs = []
	for i in range(len(files)): 
		imgs.append(read(files[i], crop=False)[1])
		# display(imgs[i], t=30)

	# vectors is list of frames containing the points in the vectors
	# tracks is a list of points tracked
	vectors, tracks = sparse(imgs)
	avg_vels = calc_avg_vel(tracks)
	graph_avgs(avg_vels)
	inst_vels = calc_inst_vel(tracks)
