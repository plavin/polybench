prog = gemver
root = ../../..
util = $(root)/utilities

include $(root)/Makefile.in

$(prog) : $(prog).o
	gcc $(CFLAGS) -o $(prog) $(prog).o $(util)/polybench.o
$(prog).o : $(prog).c
	gcc $(CFLAGS) -I$(util) -c -o $(prog).o $(prog).c

.PHONY: clean
clean :
	rm -f $(prog) $(prog).o
