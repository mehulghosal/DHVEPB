import os, time, Data
import dataProcessing as dp

directory = os.getcwd() + "/out/"

def init():
	global directory
	files = dp.initFiles(directory)
	files = dp.sortFiles(files)
	f = []
	for i in files:
		f.append(read(i))
	return f

#reads data of one output file
#return map from that file
def read(file):
	inp = file.read().split("\n")[:-1]
	data = []
	for line in inp:
		data.append(Data.Data.fromStr(line))
	return data

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data):
	m = [[0 for j in range(501)] for i in range(551)]
	for i in range(len(data)):
		d = data[i]
		m[d.lat][d.lon] = d
	return m

#f1 and f2 are maps (returned from formatMap()) of all Data points in a file
#returns map of change in values at each lat, lon
def deltaVals(f1, f2):
	#initializes 2d list 
	m = f1
	for i in range(551):
		for j in range(501):
			d1 = f1[i][j]
			d2 = f2[i][j]
			if d1 == 0 and d2 == 0:
				pass
			elif d1 == 0:
				m[i][j] = d2
			elif d2 ==0:
				m[i][j] = d1
			else:
				m[i][j] = 0
	return m

def writeMap(m, name):
	f = open(str(name), "w")
	s = ""
	for i in m:
		for j in i:
			s += str(j) + " "
		s += "\n"
	f.write(s)
	f.close()

# takes in a file - list of data objects
# returns 4 data objects - [top left, top right, bottom left, bottom right]
# assuming longitude increases from west to east & latitude increases from bottom to top
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
	f1 = (read(files[0]))

	# list of 4 corners in f1
	f1Corners = findCorners(f1)
	for i in f1Corners: print(i)