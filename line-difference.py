from shapely import to_geojson, Point, Polygon, LineString, difference, buffer
from circleSVG import  circleSVG
from polySVG import polySVG

line = LineString([(0, 0), (200, 200)])
l2 = LineString([(50, 50), (300, 300)])
d = difference(line, l2)
print(d)
# set up geometry data
poly1 = Polygon( [(10, 10), (100,0), (100,100), (0,100) ] )
poly2 = Polygon( [(0, 0), (200,0), (200,200), (0,200) ] )
polydiff = poly1.difference(poly2)
print( polydiff.svg() )
p = Point(100, 10)
p2 = Point(1, 1)
points = []
for i in range(33):
 q = Point(i * 8, i * 10)
 points.append(q)

points.append((Point(39, 39)))
p = Polygon([(20,0),(110,0),(110,111),(0,110)])

# write SVG tags
poly = ''
# poly = polySVG(d, 'blue')
lineSVG = ''
# lineSVG = polySVG(d, 'blue')
# tag = ''
# for el in points:
#  tag += circleSVG(9, el.x, el.y, 'red')
#  tag += circleSVG(2, el.x, el.y, 'blue')
 # a group tag
 # f.write('<g x="100" y="100" style="x: 100" transform="translate(80,40)" >')
 # f.write('<circle r="30" cx="30" cy="30" stroke-width="0.01mm" />')
 # f.write('</g>')

def writeSVG(fileName, content):
 fileName = 'line-difference.svg'
 f = open(fileName, 'w')
 # write the contents of the SVG file
 f.write('<svg width="400" height="400" fill="black" stroke="black">')
 f.write(content)
 f.write('</svg>')
 return 'x'

# t = '<text x="25" y="58.9" font-size="112.25" fill="black" stroke-width="0.01mm">ssss</text>'
contentStr =    polySVG(line, 'red', 22) + polySVG(l2, 'green', 6) + polySVG(d, 'yellow', 12)
# contentStr = polydiff
writeSVG('abc.svg', contentStr)