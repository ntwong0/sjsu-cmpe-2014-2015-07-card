MAP_SIZE_PIXELS          = 256

from PIL import Image
import time
import random
import signal, os
from getpid import getpid

time_start = time.time()

targetProcess = "node server.js"

pid = getpid(targetProcess)

while True:
   # time.sleep(random.randint(1,5))
    mapbytes = bytearray(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS)

    for count in range(0,MAP_SIZE_PIXELS*MAP_SIZE_PIXELS):
        x = random.randint(0,MAP_SIZE_PIXELS-1)
        y = random.randint(0,MAP_SIZE_PIXELS-1)
        try:
          mapbytes[x * (MAP_SIZE_PIXELS) + y] = random.randint(0,255);
        except IndexError:
          print "value was {}, max range is {}".format((x * (MAP_SIZE_PIXELS-1) + y),(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS))
                    
    image = Image.frombuffer('L', (MAP_SIZE_PIXELS, MAP_SIZE_PIXELS), mapbytes, 'raw', 'L', 0, 1)
    image.save("images/map.png")

    if pid == False:
        print "failure: we couldn't send our signal to the server"
        pid = getpid(targetProcess)
    else:
        try:
            #print "the following line did not work"
            #print "os.kill(int(pid),signal.SIGRTMIN)"
            #suspect SIGRTMIN is too fast for node to handle
            os.kill(int(pid),signal.SIGUSR1)
            print "success: we sent an update signal to the server"
        except OSError:
            print "failure: we couldn't send our signal to the server"
            pid = getpid(targetProcess)

    print "map created after {}".format(time.time() - time_start)
