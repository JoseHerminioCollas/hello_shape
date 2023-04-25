from shapely import LineString, difference, Point
from pointSVG import pointSVG
from writeSVG import writeSVG

p = Point(100,20)
p2 = Point(40, 50)
contentStr = pointSVG(p,  'red', 3) + \
             pointSVG(p2, 'blue', 20) + \
             pointSVG(Point(140, 150), 'green', 12)
writeSVG('point-example.svg', contentStr)
