#!/usr/bin/env python

'''
log2png.py : BreezySLAM Python demo.  Reads logfile with odometry and scan data
             from Paris Mines Tech and produces a .PNG image file showing robot 
             trajectory and final map.
             
For details see

    @inproceedings{coreslam-2010,
      author    = {Bruno Steux and Oussama El Hamzaoui},
      title     = {CoreSLAM: a SLAM Algorithm in less than 200 lines of C code},
      booktitle = {11th International Conference on Control, Automation, 
                   Robotics and Vision, ICARCV 2010, Singapore, 7-10 
                   December 2010, Proceedings},
      pages     = {1975-1979},
      publisher = {IEEE},
      year      = {2010}
    }
                 
Copyright (C) 2014 Simon D. Levy

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http://www.gnu.org/licenses/>.

Change log:

20-APR-2014 - Simon D. Levy - Get params from command line
05-JUN-2014 - SDL - get random seed from command line
'''

# Map size, scale
MAP_SIZE_PIXELS          = 800
MAP_SIZE_METERS          =  8

from breezyslam.algorithms import Deterministic_SLAM, RMHC_SLAM
from breezyslam.components import Laser
from breezyslam.robots import WheeledRobot

from dat2png_helper import MinesLaser, Rover, load_data
from progressbar import ProgressBar

from sys import argv, exit, stdout
from time import time
from parser import *

from PIL import Image


def main():
    seed = 9999
    runCount = 0
    dequeueCount = 0
    slam = RMHC_SLAM(MinesLaser(), MAP_SIZE_PIXELS, MAP_SIZE_METERS, random_seed=seed) \
           if seed \
           else Deterministic_SLAM(MinesLaser(), MAP_SIZE_PIXELS, MAP_SIZE_METERS)
    trajectory = []
    while dequeueCount < 100:
        if q.empty() == False:
            while (q.empty() == False):
                    slam.update(q.get())
                    print "%i" %dequeueCount
                    dequeueCount = dequeueCount + 1
                    x_mm, y_mm, theta_degrees = slam.getpos()    
                    trajectory.append((x_mm, y_mm))
                                    
            # Create a byte array to receive the computed maps
            mapbytes = bytearray(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS)
            
            # Get final map    
            slam.getmap(mapbytes)
            
            # Put trajectory into map as black pixels
            for coords in trajectory:
                        
                    x_mm, y_mm = coords
                                           
                    x_pix = mm2pix(x_mm)
                    y_pix = mm2pix(y_mm)
                                                                                                          
                    mapbytes[y_pix * MAP_SIZE_PIXELS + x_pix] = 0;
                            
            # Save map and trajectory as PNG file
            image = Image.frombuffer('L', (MAP_SIZE_PIXELS, MAP_SIZE_PIXELS), mapbytes, 'raw', 'L', 0, 1)
            #image.save('map%i.png' %runCount)
            image.save("map" + str(dequeueCount) + ".png")
            print "image generated"
        
            
# Helpers ---------------------------------------------------------        

def mm2pix(mm):
        
    return int(mm / (MAP_SIZE_METERS * 1000. / MAP_SIZE_PIXELS))  
    
                    
main()
