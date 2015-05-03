'''
BreezySlam adaptation

This module simulates the LIDAR collection module's output behavior.
'''

import serial
import sys
import time

def parser(list):
    ser = serial.Serial('/dev/ttyMFD1', 921600)

    chunk = (delimiter, index, dist0[0:2], dist1[0:2], dist2[0:2], dist3[0:2])
    ser.read()

def simulate_UART_packet_recv(list,packet):
    print('Loading data from %s...' % filename)
    fd = open(filename, 'rt')
    
    badScanCount = 0
    
    while True:  
        
        s = fd.readline()
        
        if len(s) == 0:
            fd.seek(0)
            continue
            
        toks = s.split()
        scan = [int(tok) for tok in toks[0:]]

        if len(scan) != 360:
            print len(scan)
            badScanCount = badScanCount + 1
        else:
            packet.append(scan)
    fd.close()
        
    return packet
