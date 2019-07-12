#class for data structure so i can kep track of all necessary info
class Data():
	#parameters
	#t is file number; lat is line number; lon is posiiton in line; v is the actual value
	def __init__(self, time, latitude, longitude, v):
		self.t = time
		self.lat = latitude
		self.lon = longitude
		self.val = v

	def __str__(self):
		return ','.join((str(self.t), str(self.lat), str(self.lon), str(self.val)))

	#pass in string tuple, returns Data object: 0,1,250,-0.00040754789
	def fromStr(s):
		s = s.split(",")
		t = int(s[0])
		la = int(s[1])
		lo = int(s[2])
		v = float(s[3])
		return Data(t, la, lo, v)

	def set_val(self, v):
		self.val = v