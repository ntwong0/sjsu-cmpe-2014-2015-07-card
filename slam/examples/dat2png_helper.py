'''
mines.py - classes for the SLAM apparatus used at Paris Mines Tech
             
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
'''

from breezyslam.robots import WheeledRobot
#?1
#from breezyslam.components import URG04LX
from breezyslam.components import XV11

import math
#+1
import random


# Method to load all from file ------------------------------------------------
# Each line in the file has the format:
#
#  TIMESTAMP  ... Q1  Q1 ... Distances
#  (usec)                    (mm)
#  0          ... 2   3  ... 24 ... 
#  
#where Q1, Q2 are odometry values

def load_data(datadir, dataset):
    
    filename = '%s/%s.dat' % (datadir, dataset)
    print('Loading data from %s...' % filename)
    
    fd = open(filename, 'rt')
    
    timestamps = []
    scans = []
    odometries = []
    
    while True:  
        
        s = fd.readline()
        
        if len(s) == 0:
            break       
            
#?1
#        toks = s.split()[0:-1] # ignore ''
        toks = s.split()

        odometry = (int(toks[0]), int(toks[2]), int(toks[3]))
#?1
#        lidar = [int(tok) for tok in toks[24:]]
        lidar = [int(tok) for tok in toks[0:]]
#+2
        for x in range(0, len(lidar)):
            lidar[x] = lidar[x] * 350
#~+1            
#            print lidar[x]
        scans.append(lidar)
        odometries.append(odometry)
        
    fd.close()
        
    return scans, odometries
#?5
#class MinesLaser(URG04LX):
#    
#    def __init__(self):
#        
#        URG04LX.__init__(self, 70, 145)
class MinesLaser(XV11):
    
    def __init__(self):
        
        XV11.__init__(self, 0, 0)
        
# Class for MinesRover custom robot ------------------------------------------

class Rover(WheeledRobot):
    
    def __init__(self):
        
        WheeledRobot.__init__(self, 77, 165)
        
        self.ticks_per_cycle = 2000
                        
    def __str__(self):
        
        return '<%s ticks_per_cycle=%d>' % (WheeledRobot.__str__(self), self.ticks_per_cycle)
        
    def computeVelocities(self, odometry):
        
        return WheeledRobot.computeVelocities(self, odometry[0], odometry[1], odometry[2])

    def extractOdometry(self, timestamp, leftWheel, rightWheel):
                
        # Convert microseconds to seconds, ticks to angles        
        return timestamp / 1e6, \
               self._ticks_to_degrees(leftWheel), \
               self._ticks_to_degrees(rightWheel)
               
    def odometryStr(self, odometry):
        
        return '<timestamp=%d usec leftWheelTicks=%d rightWheelTicks=%d>' % \
               (odometry[0], odometry[1], odometry[2])
               
    def _ticks_to_degrees(self, ticks):
        
        return ticks * (180. / self.ticks_per_cycle)
        
        
        
        
        
