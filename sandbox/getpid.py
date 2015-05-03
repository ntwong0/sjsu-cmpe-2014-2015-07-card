'''
learning python signal, os, and subprocess
see files:
	infinloop.py
	getpid.py (this file)
'''

import os
import subprocess
import signal
import time

mySearchTerm = "python infinloop.py"

def getpid(searchTerm):
	#tokenize searchTerm
	searchTermToks = searchTerm.split()

	#print "procListings from `ps -ef | grep searchTerm`""
	p1 = subprocess.Popen(['ps','-ef'], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(['grep', '{}'.format(searchTerm)], stdin=p1.stdout, stdout=subprocess.PIPE)
	p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
	procListings = p2.communicate()[0]
	
	#print "if `python searchTerm.py` is running, return PID"
	toks = procListings.split()
	searchTermIndex = 0
	for count in range(0,len(toks)):
		if(toks[count] == 'grep'):
			return False
		elif(toks[count] == searchTermToks[searchTermIndex] and searchTermIndex < len(searchTermToks)-1):
			searchTermIndex = 1
		elif(toks[count] == searchTermToks[searchTermIndex] and searchTermIndex == len(searchTermToks)-1):
			return toks[count - searchTermIndex - 6]
		else:
			searchTermIndex = 0
			
	#print "else return false"
	return False
'''
pid = getpid(mySearchTerm)
while pid == False:
	pid = getpid(mySearchTerm)

while True:
	if pid == False:
		print "oh well."
		pid = getpid(mySearchTerm)
		time.sleep(1)
	else:
		print pid
		try:
			os.kill(int(pid),signal.SIGRTMIN)
			print "we sent a signal!"
			time.sleep(1)
		except OSError:
			print "well, that didn't work"
			pid = getpid(mySearchTerm)
			time.sleep(1)
'''