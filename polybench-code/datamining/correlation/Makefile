prog = correlation
root = /nethome/plavin3/sst/polybench/polybench-code
util = $(root)/utilities

include $(root)/Makefile.in

$(prog) : $(prog).o
	gcc -D$(SIZE) $(CFLAGS) -o $(prog) $(prog).o $(util)/polybench.o
$(prog).o : $(prog).c
	gcc -D$(SIZE) $(CFLAGS) -I$(util) -c -o $(prog).o $(prog).c

.PHONY: clean
clean :
	rm -f $(prog) $(prog).o
