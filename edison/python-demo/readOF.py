import time, os

# set the filename and open the file
file = '/home/root/data/log2.txt'
fileHandle = open(file,'r')

# find the size of the file and move to the end
st_results = os.stat(file)
st_size = st_results[6]
fileHandle.seek(st_size)

while 1:
	where = fileHandle.tell()
	line = fileHandle.readline()
	if not  line:
		time.sleep(1)
		fileHandle.seek(where)
	else:
		print line
