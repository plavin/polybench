SUBDIRS := utilities stencils medley datamining linear-algebra

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

SUBCLEAN = $(addsuffix .clean,$(SUBDIRS))

clean: $(SUBCLEAN)

$(SUBCLEAN): %.clean:
	$(MAKE) -C $* clean


.PHONY: all $(SUBDIRS)
