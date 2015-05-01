'''
BreezySlam adaptation

This module simulates the LIDAR collection module's output behavior.
'''

import socket
import sys
import time

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

def simulate_UART_packet_recv(filename,packet):
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

s.listen(5)
print('Waiting for a connection.')

def threaded_client(conn):
  conn.send('Welcome, type your info\n')
  message = 0
  while True:
      data = conn.recv(2048)
      if not data:
          break
      conn.sendall(str(message))
      print "hello"
      message = message + 1
      time.sleep(5)
  conn.close()

start_new_thread()

while True:

  conn, addr = s.accept()
  print('connected to: '+addr[0]+':'+str(addr[1]))
  start_new_thread(threaded_client,(conn,))
