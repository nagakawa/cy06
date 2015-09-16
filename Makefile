fromsvg = resource/stgframe.png resource/title.png resource/nesmeja.png
ttb = $(foreach dir, $(1), $(foreach file, $(basename $(shell ls $(dir))), $(file).bin))

all: $(fromsvg) $(call ttb, language/*.txt language/*/*.txt) hele/shotc.dnh ambient/shotc.dnh ambient/shotdata.dnh

resource/%.png: resource/%.svg
	inkscape -z -e $@ $<
	racket imgtool.rkt $@
language/%.bin: language/%.txt; python3 language/genb.py $<
hele/shotc.dnh: hele/genshotc.py; python3 hele/genshotc.py > hele/shotc.dnh
ambient/shotc.dnh: ambient/genshotc.py; python3 ambient/genshotc.py > ambient/shotc.dnh
ambient/shotdata.dnh: ambient/gendata.py; python3 ambient/gendata.py > ambient/shotdata.dnh

clean:
	rm language/*.bin language/*/*.bin

yukkuri:
	@echo "ゆっくりしていってね！"