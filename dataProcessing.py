import os, time, Data, _thread
from os.path import isfile, join

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
	files = [f for f in os.listdir(directory) if isfile(join(directory, f))]
	return files

#sorts files in numeric order 1-480
def sortFiles(files, start=8, end=10):
	files.sort(key = lambda x: int(x[start:end]))
	return files

#appends the 130,000,000 data objects to dataList
#and writes to output files
def readData(f):
	files = f
	#iterates through files
	t = time.time()
	for fileIndex in range(100):
		if fileIndex != 249: continue
		file = open("./newdata"+files[fileIndex], 'r')
		print(file)
		lines = file.readlines()
		print(lines)

		a = str(fileIndex+1)
		if len(a)<10:
			a = "00" + a
		else:
			a = "0" + a
		outFile = open("./out" + a + ".txt", "w")
		for lineIndex in range(len(lines)):
			line = lines[lineIndex]
			values = line.split()
			#iterates through values in line
			for valIndex in range(len(values)):
				val = values[valIndex]
				x = float(val[:-4])
				if x >= 0: continue
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
def imdumb(l):
	#list of everything in output directory
	files = initFiles("./out")
	a = []
	c=0
	for f in files:
		# if not c%2==l: continue
		c+=1
		fi = open('./out/'+f)
		data = fi.read().split("\n")[:-1]
		print(data)
		x = ""
		for d in data:
			da = Data.Data.fromStr(d)
			if da.val < 0:
				x += str(da) + "\n"
		a.append(x)

	# print(a)
	for i in range(len(files)):
		# if not i%2==l: continue
		t = str(i)
		if len(t) == 1:
			t = "00"+t
		elif len(a) == 2:
			t = "0" +t
		fi = open('./out/out' + t + ".txt", "w")
		fi.write(a[i])

if __name__ == '__main__':
	imdumb(1)
	print("done")