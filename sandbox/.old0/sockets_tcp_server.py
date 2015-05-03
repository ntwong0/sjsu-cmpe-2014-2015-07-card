import socket
import sys
import time
#from _thread import *
from thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
		s.bind((host, port))
except socket.error as e:
		print(str(e))

connlist = []

s.listen(5)
print('Waiting for a connection.')
def threaded_client(connlist,conn):
	#conn.send(str.encode('Welcome, type your info\n'))
	conn.send('Welcome, type your info\n')
	message = 0
	while True:
			data = conn.recv(2048)
			#reply = 'Server output: '+ data.decode('utf-8')
			#reply = 'Server output: '+ data
			if not data:
					break
			conn.sendall(str(message))
			print "hello"
			message = message + 1
			time.sleep(5)
	conn.close()

while True:

	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))
	connlist.append(addr)
	start_new_thread(threaded_client,(connlist,conn,))
