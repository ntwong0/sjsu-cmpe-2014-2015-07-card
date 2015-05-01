# Blinking LED demo c++ demo
# gcc compiler
CC=gcc
# Object Compiler options
OFLAGS=-lmraa -c -Wall
# Linker Options
CFLAGS=-lmraa -Wall
all: demo

demo: demo.o
	$(CC) $(CFLAGS) demo.o -o demo

demo.o: demo.c
	$(CC) $(OFLAGS) demo.c

clean:
	rm -rf *.o demo
