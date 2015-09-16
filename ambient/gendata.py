delay_colors = [
	(182, 182, 182),
	(255, 99, 99),
	(255, 103, 99),
	(255, 99, 155),
	(255, 99, 235),
	(168, 99, 255),
	(103, 99, 255),
	(99, 237, 255),
	(161, 236, 236),
	(99, 255, 105),
	(206, 255, 99),
	(255, 174, 99),
	(198, 255, 132),
	(255, 254, 99),
	(157, 214, 140),
	(177, 177, 177)
]

print("#UserShotData")
print('shot_image = "./shotsheet.png"')

for row in range(0, 11):
	for col in range(0, 16):
		print("ShotData {")
		print("	id = {0}".format(400 + 16 * row + col))
		print("	rect = ({0}, {1}, {2}, {3})".format(
			16 * col, 16 * row,
			16 * col + 16, 16 * row + 16
		))
		print("	delay_color = {0}".format(delay_colors[col]))
		print("}")