#!/usr/bin/python

flag = 0
lastIndex = False
firstLine = True
lookAhead = 0

#ser = serial.Serial('/dev/ttyMFD1', 921600)
f = open('testingSerialLog.txt', 'r')
count = 0

while count < 1000:
        count = count + 1
        word = f.read(1)
        if(word == '\xfa' and flag == 0):
                flag = flag + 1

        elif((ord(word) in range(160,250)) and flag == 1):
                if(word != '\xf9' and firstLine):
                        lastIndex = False
                        flag = 0
                elif(word == '\xf9' and firstLine):
                        lastIndex = False
                        firstLine = False
                        flag = 0
                        lookAhead = ord('\xa0')
                elif(word == '\xf9' and not firstLine):
                        if(ord(word) == lookAhead):
                                lastIndex = True
                                flag = flag + 1
                                lookAhead = ord('\xa0')
                                print hex(ord(word)),
                        else:
                                print hex(lookAhead),
                                print "0 0 0 0",                                
                                lastIndex = True
                                flag = flag + 1
                                lookAhead = ord('\xa0')
                                print hex(ord(word)),
                else:
                        if(ord(word) == lookAhead):
                                lastIndex = False
                                flag = flag + 1
                                lookAhead = ord(word) + 1
                                print hex(ord(word)),
                        else:
                                print hex(lookAhead),
                                print "0 0 0 0",
                                lastIndex = False
                                flag = flag + 1
                                lookAhead = ord(word) + 1
                                print hex(ord(word)),        
        
	elif(flag in range(2,10)):
                if(flag%2 == 0):
                        temp = word
                        flag = flag + 1
                        continue
                else:
                        flag = flag + 1

                        if(flag == 10 and lastIndex):
                                print (((ord(word) << 8) + ord(word)))
                                temp = ""
                                flag = 0
                                lastIndex = False
                        elif(flag == 10):
                                print (((ord(word) << 8) + ord(word))),
                                temp = ""
                                flag = 0
                        else:
                                print (((ord(word) << 8) + ord(word))),
				temp = ""
f.close()