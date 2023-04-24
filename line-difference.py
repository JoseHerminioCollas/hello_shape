from shapely import LineString, difference
from lineStringSVG import lineStringSVG
from writeSVG import writeSVG

line = LineString([(0, 0), (200, 200)])
l2 = LineString([(50, 50), (300, 300)])
d = difference(line, l2)
contentStr = lineStringSVG(line, 'red', 22) +\
             lineStringSVG(l2, 'green', 6)  \
             + lineStringSVG(d, 'yellow', 12)
writeSVG('abc.svg', contentStr)
