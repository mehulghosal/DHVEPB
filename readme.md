this will be the directory where i will put my science research work
i might at a fiture date put this on github - who knows

so the original data Dr. P sent me is in data.mat - this is a mat file, and i don't have matlab
so i processed that data using scipy.io.readmat(), wrote the data to different files as dicts
this located in dir olddata
this actually worked, but he sent me new data in text files

the new data is located in the dir newdata
"There are 480 txt files (each corresponds to each point in time_save).
Each txt file contains 551 lines (each corresponds to different latitude listed in lat_save)
and each line contains 501 numbers (each corresponds to different longitude)."
so im gonna create a new python script just to store the values in some way - idk theres a lot of data points (132,504,480)


so from just a quick glance at some of the data files - it looks like theres mostly variation in longitudes of the disturbances
looks like theres only important stuff in the middle fo the line - so corresponds to middlish long - near equator

11/8 parsed string values into floats  -only for first line of first file

11/9 so the files in the list are out of order - how do i sort them ??
	at least ik that theyre in the same order every time i run the script

11/12
lol ok so im just gonna take a real bad attempt at sorting the list

11/22
so i was writing my readData() functions to append each data point to the list
i like git stashed a few times, but apparently, it seemed to work, but i think i stopped the function b4 it finished
i only have files 0-414
so i can probably run the script for fileIndices >414

ok seems like i got it

got to make some gui? maybe with pygame

11/26 
lol ok so i dont know/dont want to know pygame that well - so I'll just do the velocity thing 
im going to find the lat and long average of each file and where they r located --> look in my journal i have notes about how/what im doing

11/28 
finally pushed to git repo
.gitignore has all of the data files, so I can actually upload the directory on github

11/29
i need a 2d list - height is the len(range of lat values), length is the len(range of long values)
range of where nonzero values occur


leftmost		rightmost
long 			longitude

[ [a, b, c, d, e, ...], -- highest lat
  [a1, b1, c1, d1,...],
  [a2, b2, c2, d2,...],
  [...]					-- lowest lat
]