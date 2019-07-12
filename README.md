## Deriving Horizontal Velocities of Equatorial Plasma Bubbles
* goal of this project is to find horizontal drift velocities based on differences in total electron content over time
* acknowledgements to Dr. R. Pradipta for support and providing the data

### data:
* 480 txt files (each corresponds to a point in time; increment 3 mins apart)
* Each txt file contains 551 lines (each corresponds to different latitude; increment by 0.2°)
* and each line contains 501 numbers (each column corresponds to different longitude; increment by 0.2°)
* each value is a TEC reading at that location and time; one unit is 10<sup>16</sup> electrons/m<sup>2</sup>
	* negative values represent depletions

* note: data in input & output files not published on github because of size limitations

### data processing
* in dataProcessing.py, raw data is read in and converted to Data objects
* these Data objects are then pruned, and any with a value == 0 are deleted
* printed to files coresponding to input files in /output --> for later use

### analyzing
* read in data objects again from output
* generate images basde on files
* using optical flow to give motion vectors to images ~ treat like a video
* color correlates to direction: blue is left, red is right, green is up, purple is down