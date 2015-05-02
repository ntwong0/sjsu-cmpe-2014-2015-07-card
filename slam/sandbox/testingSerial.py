import serial

ser = serial.Serial('/dev/ttyMFD1',921600)
count = 0

while count < 36000:
	f = open('testingSerialLog.txt', 'a')
	f.write(ser.read())
	f.close()
	count = count + 1
