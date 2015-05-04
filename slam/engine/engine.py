#!/usr/bin/env python

'''
engine.py :  BreezySLAM engine adapted from code by Simon D. Levy

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
'''

# Map size, scale
MAP_SIZE_PIXELS          = 1600
MAP_SIZE_METERS          = 32

from breezyslam.algorithms import Deterministic_SLAM, RMHC_SLAM
from breezyslam.components import Laser, XV11

from sys import argv, exit, stdout
from time import time
from parser import *

import signal, os
from getpid import getpid

from PIL import Image

def main():
    print "initiating engine..."
    seed = 9999
    dequeueCount = 0
    time_start = time.time()
    targetProcess = "node server.js"
    targetSignal = signal.SIGUSR1
    serverMinTimeDelay = 5

    pid = getpid(targetProcess)
    slam = RMHC_SLAM(MinesLaser(), MAP_SIZE_PIXELS, MAP_SIZE_METERS, random_seed=seed) \
        if seed \
        else Deterministic_SLAM(MinesLaser(), MAP_SIZE_PIXELS, MAP_SIZE_METERS)
    trajectory = []
    
    while time.time() - time_start < 600:
        time_thisLoop = time.time()
        if not q.empty():
            while (not q.empty()):
                slam.update(q.get())
                dequeueCount = dequeueCount + 1
                x_mm, y_mm, theta_degrees = slam.getpos()    
                trajectory.append((x_mm, y_mm))
                                        
            # Create a byte array to receive the computed maps
            mapbytes = bytearray(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS)
            
            # Get map from this batch
            slam.getmap(mapbytes)
            
            # Put trajectory into map as black pixels
            for coords in trajectory:
                        
                x_mm, y_mm = coords
                                       
                x_pix = mm2pix(x_mm)
                y_pix = mm2pix(y_mm)
                                                                                                      
                mapbytes[y_pix * MAP_SIZE_PIXELS + x_pix] = 0;
                            
            # Save map and trajectory as PNG file
            image = Image.frombuffer('L', (MAP_SIZE_PIXELS, MAP_SIZE_PIXELS), mapbytes, 'raw', 'L', 0, 1)
            image.save("../../webgui/images/" + "map" + ".png")
            print "map created after {} scans".format(dequeueCount)

            # Try to tell the server
            if pid == False:
                print "failure: no server pid"
                pid = getpid(targetProcess)
            else:
                try:
                    os.kill(int(pid),targetSignal)
                    print "success: signal sent to server"
                except OSError:
                    print "error: whoops, just lost the pid"
                    pid = getpid(targetProcess)

            # give the server at least serverMinTimeDelay seconds to catch up
            while time.time() - time_thisLoop < serverMinTimeDelay:
                ()
        
            
# Helpers ---------------------------------------------------------        

def mm2pix(mm):
        
    return int(mm / (MAP_SIZE_METERS * 1000. / MAP_SIZE_PIXELS))  
    
class MinesLaser(XV11):
    
    def __init__(self):
        
        XV11.__init__(self, 0, 0)
                    
main()
