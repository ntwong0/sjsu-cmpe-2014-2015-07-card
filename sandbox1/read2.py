import serial
ser = serial.Serial('/dev/ttyMFD1', 921600)
f = open('testingSerialLog.txt', 'w')
count = 0
while count < 1000:
        f.write(ser.read())
	count = count + 1
f.close()
