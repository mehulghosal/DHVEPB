import os, time, Data, _thread, cv2
import matplotlib.pyplot as plt
from os.path import isfile, join

#list of files
files = []
#lol this will be fun wont it
#list of all data values that arent 0
dataList = []

#appends datafiles as file objects to list
#modifies gloabal var files
def initFiles(directory):
	global files
	#directory = "/home/mehulghosal/code/sciresearch/newdata"
	files = [f for f in os.listdir(directory) if isfile(join(directory, f))]
	return files

#sorts files in numeric order 1-480
def sortFiles(files, start=4, end=-4):
	files.sort(key = lambda x: int(x[start:end]))
	return files

# takes in a dataMap and saves it as a cv2 image
def save(img, name):
	cv2.imwrite(str(name),img)

def display(img, name="img", t=0, mat=False):
	if mat:
		plt.imshow(img)
		plt.show()
		return
	cv2.imshow(name, img)
	if cv2.waitKey(t) & 0xff == 27:
		cv2.destroyAllWindows()

# gray==False: cvt2bgr
def cvtColor(img, gray=True):
	if gray:
		return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	else: return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#appends the 130,000,000 data objects to dataList
#and writes to output files
def readData(files):
	#iterates through files
	t = time.time()
	for fileIndex in range(len(files)):
		file = open("./data/"+files[fileIndex], 'r')
		print(file)
		lines = file.readlines()
		li = ''
		outFile = open("./out/" + files[fileIndex][-7:-4] + ".txt", "w")
		for lineIndex in range(len(lines)):
			line = lines[lineIndex]
			values = line.split()
			#iterates through values in line
			for valIndex in range(len(values)):
				val = values[valIndex]
				x = float(val)
				if x >= 0: continue
				data = Data.Data(fileIndex, lineIndex, valIndex, x)
				dataList.append(data)
				li += str(data) + ' '
			li = li[:-1] + '\n'
		outFile.write(li[:-1])

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
	files = initFiles("./out/")
	a = []
	for f in files:
		fi = open('./out/'+f, 'r+')
		data = fi.read().split("\n")[:-1]
		x = ""
		for d in data:
			da = Data.Data.fromStr(d)
			if da.val < 0:
				x += str(da) + "\n"
		os.remove('./out/'+f)
		a.append(x)
		# if a.index(x) == 10: break

	# print(a)
	
	for i in range(len(files)):
		y = str(i)
		if len(y)==1: 
			y='00'+y
		elif len(y)==2: 
			y='0'+y
		fi = open('./out/out' + y + ".txt", "w")
		fi.write(a[i])

if __name__ == '__main__':
	files = sortFiles(initFiles('./data/'), start=-7, end=-4)
	readData(files)