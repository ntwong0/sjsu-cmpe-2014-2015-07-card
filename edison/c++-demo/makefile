# Blinking LED demo c++ demo
# g++ compiler
CC=g++
# Object Compiler options
OFLAGS=-lmraa -c -Wall
# Linker Options
CFLAGS=-lmraa -Wall
all: demo

demo: demo.o
	$(CC) $(CFLAGS) demo.o -o demo

demo.o: demo.cpp
	$(CC) $(OFLAGS) demo.cpp

clean:
	rm -rf *.o demo
