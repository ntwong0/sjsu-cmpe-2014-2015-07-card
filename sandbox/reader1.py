import parser1

log = open('aLog.txt','w')

while True:
	if(q.empty() == False):
		packet = q.get()
		#print len(packet)
		log.write(len(packet))
		#print packet
		log.write(str(packet))
