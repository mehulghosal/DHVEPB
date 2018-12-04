import os, time, Data, pygame
import dataProcessing as dp

directory = "/home/mehulghosal/code/sciresearch/output/"
#this will be a 2d list, each entry will be a file
data = []

def readOutputs(files):
	global data
	for file in files:
		f =[]
		inp = files[0].read().split("\n")[:-1]
		for line in inp:
			splitLine = line.split(",")
			f.append(Data.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))
		data.append(f)

#return a map of delta vals- see readme at 11/29
def totalDelta():
	m = [[Data.Data(0, 0, 0, 0) for j in range(501)] for i in range(551)]
	for f in data:
		for d in f:
			da = m[d.lat][d.lon]
			da.lat = d.lat
			da.lon = d.lon
			da.val -= d.val

	return m

#f1 and f2 are lists of all Data points in a file
#returns map of change in values at each lat, lon
def deltaVals(f1, f2):
	#initializes 2d list 
	m = [[Data.Data((data.index(f1)+data.index(f2))/2, i, j, 0) for j in range(1, 502)] for i in range(1, 552)]
	print(len(f1))
	return m

#go through data list
#call deltavals for each consecutive pair of frames 
#store maps in list

def calc():
	deltamaps = []
	for i in range(len(data)-2):
		deltamaps.append(deltaVals(data[i], data[i+1]))
	return deltamaps

def writeMap(m, name):
	f = open(str(name), "w")
	s = ""
	for i in m:
		for j in i:
			s += str(j.val) + " "
		s += "\n"
	f.write(s)
	f.close()

#takes in map
#returns list of tueples
#index 0: pygame.rect objects --> pygame.Rect(x, y, width, height)
#index 1: value 
def initRects(m):
	r = []
	for i in m:
		for j in i:
			r.append((pygame.Rect(j.lon + 25, j.lat + 25, 1, 1), j.val))

def draw(r):
	pygame.init()
	size = (551, 601)
	screen = pygame.display.set_mode(size)
	done = False
	screen.fill((255, 255, 255))

	for rect in r:

		if rect[1] > 0: color = (255, 0, 0)
		elif rect[1] < 0: color = (0, 255, 0)
		else: color = (0, 0, 0)
		pygame.draw.rect(screen, color, rect[0])

	pygame.display.flip()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				break


if __name__ == "__main__":
	files = dp.initFiles(directory)
	files = dp.sortFiles(files)
	# readFirstFile()
	print(data)
	readOutputs(files)
	m = calc()
	for i in m:
		draw(initRects(m))

	dp.closeFiles(files)

