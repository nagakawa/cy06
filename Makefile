fromsvg = resource/stgframe.png

all: $(fromsvg) language/*.bin language/*/*.bin

resource/%.png: resource/%.svg; inkscape -z -e $@ $<
language/%.bin: language/%.txt; python3 language/genb.py $<
language/%/%.bin: language/%/%.txt; python3 language/genb.py $< 

clean:
	rm language/*.bin
