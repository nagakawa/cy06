fromsvg = resource/stgframe.png resource/title.png
ttb = $(foreach dir, $(1), $(foreach file, $(basename $(shell ls $(dir))), $(file).bin))

all: $(fromsvg) $(call ttb, language/*.txt language/*/*.txt) hele/shotc.dnh

resource/%.png: resource/%.svg
	inkscape -z -e $@ $<
	racket imgtool.rkt $@
language/%.bin: language/%.txt; python3 language/genb.py $<
hele/shotc.dnh: hele/genshotc.py; python3 hele/genshotc.py > hele/shotc.dnh

clean:
	rm language/*.bin language/*/*.bin

yukkuri:
	@echo "ゆっくりしていってね！"