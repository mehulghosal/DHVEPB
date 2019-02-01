# Deriving Horizantal Velocities of Equatorial Plasma Bubbles
* goal of this project is to find horizantal drift velocities based on differences in total electron content over time
* thank you to Dr. R. Pradipta for support and providing the data

## data:
* 480 txt files (each corresponds to a point in time)
* Each txt file contains 551 lines (each corresponds to different latitude)
* and each line contains 501 numbers (each column corresponds to different longitude)
* each value is a TEC reading at that location and time

* note: data in input & output files not published on github because of size limitations

## data processing
* in dataProcessing.py, raw data is read in and converted to Data objects
* these Data objects are then pruned, and any with a value == 0 are deleted
* printed to files coresponding to input files in /output --> for later use

* use Pickle? for object persistence: 
	* https://www.thoughtco.com/using-pickle-to-save-objects-2813661
	* https://docs.python.org/3/library/persistence.html

## analyzing
* read in data objects again from output
* create a map of the values
* then find delta TEC between th frames
	* past trouble involved memory overloading - only load in some files at a time to find differences
	* Dr. P also mentioned to look at library he sent me
		* https://dtcwt.readthedocs.io/en/0.12.0/registration.html#using-the-implementation

