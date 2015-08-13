# Generate shot constants for Hele's shotsheet
colors = ["GRAY", "RED", "LIGHTRED", "PURPLE", "PINK", "DARKBLUE", "BLUE",
          "MINT", "AQUA", "GREEN", "TEAL", "LIME", "SWAMPGREEN",
          "YELLOW", "ORANGE", "WHITE"]
identity = range(0, 16)
laserColors = [0, 1, 4, 6, 8, 11, 13, 14]
starColors = [15, 1, 3, 6, 8, 9, 13]
darkDotColors = [0, 1, 4, 6, 8, 10, 12, 14, 15]
retroStarColors = [1, 6, 9, 13]
bubbleColors = [1, 6, 9, 13, 8, 3, 14, 0]
orinColors = [1, 6, 9, 3, 13, 14, 8, 15]
mikoColors = [0, 1, 3, 6, 8, 9, 13, 15]
iceColors = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14]
kunaiColors = [0, 1, 2, 3, 4, 6, 5, 8, 9, 10, 11, 13, 14]
amuletColors = [0, 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
rriceColors = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suppositoryColors = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14]


# Use like pcd("BALL_S_{0}", 1, 1)
def pcd(formatter, color, constant):
  constantName = formatter.format(colors[color])
  print("let {0} = {1};".format(constantName, constant))

def pcds(constOffset, offsetArray, formatter, count=None):
  if not count: count = len(offsetArray)
  for i in range(0, count):
    pcd(formatter, offsetArray[i], constOffset + i)

pcds(267, laserColors, "BEAM_{0}")
pcds(1, laserColors, "RBEAM_{0}")
pcds(9, identity, "SCALE_{0}", 15)
pcds(24, identity, "BALL_DS_{0}", 15)
pcds(39, identity, "BALL_S_{0}", 15)
pcds(54, identity, "RICE_S_{0}", 15)
pcds(69, kunaiColors, "KUNAI_{0}")
pcds(82, iceColors, "ICE_{0}")
pcds(95, amuletColors, "AMULET_{0}")
pcds(108, suppositoryColors, "SUPPOSITORY_{0}")
pcds(120, rriceColors, "RICE_R_{0}")
pcds(134, identity, "STAR_S_{0}", 15)
pcds(149, starColors, "LIGHT_M_{0}")
pcds(170, darkDotColors, "BALL_SS_R_{0}")
pcds(179, identity, "DROPLET_{0}", 15)
pcds(194, starColors, "STAR_M_{0}")
pcds(263, retroStarColors, "STAR_M_RETRO_{0}")
pcds(201, starColors, "BALL_M_{0}")
pcds(208, starColors, "BUTTERFLY_{0}")
pcds(215, starColors, "KNIFE_{0}")
pcds(222, starColors, "RICE_M_{0}")
pcds(229, bubbleColors, "BALL_L_{0}")
pcds(239, orinColors, "LIGHT_S_{0}")
pcds(273, mikoColors, "LIGHT_L_{0}")
