import socket
import sys
import time
#from _thread import *
from thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.connect((host, port))
while True:
		data = s.recv(1024)
		if not data:
				break
		print 'Received: ', repr(data)
		s.sendall('ack')
		time.sleep(5)
s.close()