import pygame, os, time
import dataProcessing

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
			f.append(dataProcessing.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))
		data.append(f)

def readFirstFile():
	global data
	inp = files[0].read().split("\n")[:-1]
	for line in inp:
		splitLine = line.split(",")
		data.append(dataProcessing.Data(int(splitLine[0][1:]), int(splitLine[1][1:]), int(splitLine[2][1:]), float(splitLine[3][1:-1])))

def sortFiles(files):
	newList = []
	for f in files:
		newList.append(str(f).split("'")[1])
	#this is a list of file names as strings
	newList.sort()
	dataProcessing.closeFiles(files)
	files = []
	#re-adds each file into files in alphabetical order
	for fname in newList:
		#fname is in format: "<_io.TextIOWrapper name='newdata/dtec2dmap_11344_epoch467.txt' mode='r' encoding='UTF-8'>"
		#print(fname)
		#name = fname[33:-28] #this splices fname --> "newdata....txt"
		files.append(open(fname, "r"))
	#this should leave files as sorted

	return files

#call this fucnction every two seconds to creaete a pseudo animation 
#param file is a sublist contained in 2d list data
def initRects(file):
	#list of pygame rect objects
	#i can go through this after generating them 
	rects = []
	for val in file:
		y = val.lat
		x = val.lon
		#adding 25 to center it
		#i have a 25 px border on each side
		rects.append(pygame.Rect(x+25, y+25, 2, 2))
	return rects

#param files is 2d list data
def draw(data):
	pygame.init()

	#im having 50 px of white space in both dimensions
	#so i have a 25 px border on each side
	size = (551, 601)
	screen = pygame.display.set_mode(size)
	done = False

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		screen.fill((255,255,255))
		for d in data:
			rects = initRects(d)
			for rect in rects:
				pygame.draw.rect(screen, (0, 0, 0), rect)
			print(file)
			# time.sleep(2)

		pygame.display.flip()


if __name__ == "__main__":
	files = dataProcessing.initFiles(directory)
	files = sortFiles(files)
	# readFirstFile()
	readOutputs(files)
	draw(data)
	dataProcessing.closeFiles(files)

