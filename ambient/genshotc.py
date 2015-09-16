row_names = [
	"WTFLASER", "CHEVRON", "DONUT", "MARBLE",
	"RICE2", "KUNAI2", "DIAMOND", "AMULET2",
	"BLOSSOM", "RICE3", "HEART"
]

color_names = [
	"WHITE", "RED", "SCARLET", "PINK",
	"MAGENTA", "PURPLE", "BLUE", "MINT",
	"AQUA", "GREEN", "LIME", "ORANGE",
	"BROWN", "YELLOW", "SWAMP", "GRAY"
]

for row in range(0, 11):
	for col in range(0, 16):
		print("let {0}_{1} = {2};".format(row_names[row], color_names[col], 400 + 16 * row + col))