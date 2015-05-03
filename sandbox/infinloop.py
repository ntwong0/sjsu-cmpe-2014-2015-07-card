'''
learning python signal, os, and subprocess
see files:
	infinloop.py (this file)
	getpid.py
'''

import signal

def signal_handler(signum,stackframe):
	print "okay, I'll update."

signal.signal(signal.SIGRTMIN, signal_handler)

while True:
	()