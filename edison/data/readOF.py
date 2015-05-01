#!/usr/bin/python
import time, os

list = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","AA","AB","AC","AD","AE","AF",
        "B0","B1","B2","B3","B4","B5","B6","B7","B8","B9","BA","BB","BC","BD","BE","BF",
        "C0","C1","C2","C3","C4","C5","C6","C7","C8","C9","CA","CB","CC","CD","CE","CF",
        "D0","D1","D2","D3","D4","D5","D6","D7","D8","D9","DA","DB","DC","DD","DE","DF",
        "E0","E1","E2","E3","E4","E5","E6","E7","E8","E9","EA","EB","EC","ED","EE","EF",
        "F0","F1","F2","F3","F4","F5","F6","F7","F8","F9"]

flag = 0
lastIndex = False
firstLine = True

# set the filename and open the file
file = '/home/root/data/eduardo.txt'
fileHandle = open(file,'r')

# find the size of the file and move to the end
st_results = os.stat(file)
st_size = st_results[6]
fileHandle.seek(st_size)

while 1:
	where = fileHandle.tell()
	data = fileHandle.readline()
	firstLine = True 	

	if not data:
		print "Sleeping"
		time.sleep(1)
		fileHandle.seek(where)
	else:
		print "IN THE ELSE STATEMENT"
        	for line in data:
                	words = line.split()[0:]
	        for word in words:
        	 	if(word == "FA" and flag == 0):
                	        flag = flag + 1
	              	
			elif((word in list) and flag == 1):
                        	if(word != "F9" and firstLine):
                                	lastIndex = False
                                	flag = 0
                        
				elif(word == "F9" and firstLine):
                                	lastIndex = False
                                	firstLine = False
                                	flag = 0
                        	elif(word == "F9" and not firstLine):
                                	print word,
                                	lastIndex = True
                                	flag = flag + 1
                        	else:
                                	print word,
                                	flag = flag + 1
		
			elif(flag in range(2,10)):
                        	if(flag%2 == 0):
                                	temp = word
                                	flag = flag + 1
                                	continue
                       		else:
                                	temp = temp + word
                                	flag = flag + 1

                                	if(flag == 10 and lastIndex):
                                        	print int("0x"+temp,16)
                                        	temp = ""
                                        	flag = 0
                                        	lastIndex = False
                                	
					elif(flag == 10):
                                        	print int("0x"+temp,16),
                                        	temp = ""
                                        	flag = 0
                                	
					else:
                                        	print int("0x"+temp,16),
						temp = ""
		
