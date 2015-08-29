fromsvg = resource/stgframe.png resource/title.png
ttb = $(foreach dir, $(1), $(foreach file, $(basename $(shell ls $(dir))), $(file).bin))

all: $(fromsvg) $(call ttb, language/*.txt language/*/*.txt)

resource/%.png: resource/%.svg; inkscape -z -e $@ $<
language/%.bin: language/%.txt; python3 language/genb.py $<
#language/%/%.bin: language/%/%.txt; python3 language/genb.py $< 

clean:
	rm language/*.bin language/*/*.bin

yukkuri:
	@echo "ゆっくりしていってね！"