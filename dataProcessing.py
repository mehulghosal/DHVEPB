import os, time, Data

#list of files
files = []
#lol this will be fun wont it
#list of all data values that arent 0
dataList = []

#appends datafiles as file objects to list
#modifies gloabal var files
def initFiles(directory, t = "r"):
	global files
	#directory = "/home/mehulghosal/code/sciresearch/newdata"
	for root, dirs, filenames in os.walk(directory):
		for f in filenames:
			file = open(directory+f, t)
			files.append(file)
	return files

#sorts files in numeric order 1-480
def sortFiles(files):
	newList = []
	for f in files:
		newList.append(str(f).split("'")[1])
	#this is a list of file names as strings
	newList.sort()
	closeFiles(files)
	files = []
	#re-adds each file into files in alphabetical order
	for fname in newList:
		#fname is in format: "<_io.TextIOWrapper name='newdata/dtec2dmap_11344_epoch467.txt' mode='r' encoding='UTF-8'>"
		#name = fname[33:-28] #this splices fname --> "newdata....txt"
		files.append(open(fname, "r"))
	#this should leave files as sorted

	return files

#appends the 130,000,000 data objects to dataList
#and writes to output files
def readData():
	global dataList, files
	#iterates through files
	t = time.time()
	for fileIndex in range(len(files)):
		if fileIndex != 249: continue
		file = files[fileIndex]
		#list of strings of each lines
		lines = file.readlines()
		#if fileIndex < 414: continue

		outFile = open("/home/mehulghosal/code/sciresearch/output/out" + str(fileIndex+1) + ".txt", "w")
		for lineIndex in range(len(lines)):
			line = lines[lineIndex]
			values = line.split()
			#iterates through values in line
			for valIndex in range(len(values)):
				val = values[valIndex]
				x = float(val[:-4])
				if x == 0: continue
				exp = 10**int(val[-3:])
				#adding one to all indices to eliminate 0, and go up to 480
				data = Data.Data(fileIndex + 1, lineIndex + 1, valIndex + 1, x*exp)
				dataList.append(data)
				outFile.write(str(data) + "\n")
		print(fileIndex)
	print("time required is: " + str(time.time() - t))
	return dataList

#closes all files to prevent memory leaks
#param is list of files
def closeFiles(files):
	for file in files:
		file.close()

#prunes all non-negative values
def imdumb():
	#list of everything in output directory
	files = sortFiles(initFiles("/home/mehulghosal/code/sciresearch/output/"))
	a = []
	for f in files:
		data = f.read().split("\n")[:-1]
		x = ""
		for d in data:
			x += str(Data.Data.fromStr(d)) + "\n"
		a.append(x)

	b = "/home/mehulghosal/code/sciresearch/out/"
	for i in range(1, 552):
		f = open("out" + i + ".txt", "w")
		f.write(a[i-1])


if __name__ == '__main__':
	t = time.time()
	# initFiles("/home/mehulghosal/code/sciresearch/newdata/")
	# sortFiles(files, direc)
	imdumb()
	closeFiles(files)
	print(time.time()- t)

