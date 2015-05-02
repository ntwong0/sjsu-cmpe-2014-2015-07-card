from thread import *
import Queue

q = Queue.Queue(2048)

log = open('aLog.txt','w')

def parser():

        flag = 0
        lastIndex = False
        firstLine = True
        lookAhead = 0
        packet = []

        #ser = serial.Serial('/dev/ttyMFD1', 921600)
        ser = open('testingSerialLog.txt', 'r')

        while True:
                word = ser.read(1)
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
                                        #print hex(ord(word)),
                                else:
                                        #print hex(lookAhead),
                                        print "0 0 0 0",                                
                                        for x in range(0,4):
                                                packet.append(0)
                                        lastIndex = True
                                        flag = flag + 1
                                        lookAhead = ord('\xa0')
                                        #print hex(ord(word)),
                        else:
                                if(ord(word) == lookAhead):
                                        lastIndex = False
                                        flag = flag + 1
                                        lookAhead = ord(word) + 1
                                        #print hex(ord(word)),
                                else:
                                        #print hex(lookAhead),
                                        print "0 0 0 0",
                                        for x in range(0,4):
                                                packet.append(0)
                                        lastIndex = False
                                        flag = flag + 1
                                        lookAhead = ord(word) + 1
                                        #print hex(ord(word)),        
                
        	elif(flag in range(2,10)):
                        if(flag%2 == 0):
                                temp = word
                                flag = flag + 1
                                continue
                        else:
                                flag = flag + 1

                                if(flag == 10 and lastIndex):
                                        print (((ord(temp) << 8) + ord(word)))
                                        packet.append(((ord(temp) << 8) + ord(word)))
                                        temp = ""
                                        flag = 0
                                        if(q.full() == False):
                                                q.put(packet)
                                        print len(packet)
                                        packet = []
                                        lastIndex = False
                                elif(flag == 10):
                                        print (((ord(temp) << 8) + ord(word))),
                                        packet.append(((ord(temp) << 8) + ord(word)))
                                        temp = ""
                                        flag = 0
                                else:
                                        print (((ord(temp) << 8) + ord(word))),
                                        packet.append(((ord(temp) << 8) + ord(word)))
        				temp = ""

start_new_thread(parser,())

while True:
	if(q.empty() == False):
		packet = q.get()
		#print len(packet)
		log.write(str(len(packet)))
		#print packet
		log.write(str(packet))
