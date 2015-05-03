import socket
import sys
#from _thread import *
from thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

try:
		s.bind((host, port))
except socket.error as e:
		print(str(e))

while 1:
		data, addr = s.recvfrom(1024)
		message = 'broadcasting received message: \"{}\", from {}'.format(data.rstrip('\n'), addr)
		print message
		s.sendto(message, (addr[0], addr[1]))

'''
s.listen(5)
print('Waiting for a connection.')

def threaded_client(conn):
	#conn.send(str.encode('Welcome, type your info\n'))
	conn.send('Welcome, type your info\n')

	while True:
			data = conn.recv(2048)
			#reply = 'Server output: '+ data.decode('utf-8')
			reply = 'Server output: '+ data
			if not data:
					break
			#conn.sendall(str.encode(reply))
			conn.sendto(data, ('<broadcast>, port'))
	conn.close()

while True:

	box = []
	conn, addr = s.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))

	start_new_thread(threaded_client,(conn,))
'''
