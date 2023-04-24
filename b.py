from shapely import to_geojson, Point, Polygon, buffer
from circleSVG import  circleSVG
from polySVG import polySVG

poly1 = Polygon( [(0, 0), (100,0), (100,100), (0,100) ] )
poly2 = Polygon( [(100.25, 100.25), (300.5,120.25), (301.5,201.5), (0.25,310.5) ] )
polydiff = poly1.difference(poly2)
p = Point(100, 10)
p2 = Point(1, 1)
points = []
for i in range(33):
 q = Point(i * 8, i * 10)
 points.append(q)

points.append((Point(39, 39)))
p = Polygon([(20,0),(110,0),(110,111),(0,110)])

poly = polySVG(p, 'blue')
tag = ''
for el in points:
 tag += circleSVG(9, el.x, el.y, 'red')
 tag += circleSVG(2, el.x, el.y, 'blue')

fileName = 'kkk.svg'
f = open(fileName, 'w')
# write the contents of the SVG file
f.write('<svg width="400" height="400" fill="black" stroke="black">')
f.write(poly)
f.write(tag)
f.write((poly2.svg()))
f.write('<text x="25" y="58.9" font-size="112.25" fill="black" stroke-width="0.01mm">ssss</text>')
f.write('<g x="100" y="100" style="x: 100" transform="translate(80,40)" >')
f.write('<circle r="30" cx="30" cy="30" stroke-width="0.01mm" />')
f.write('</g>')
f.write('</svg>')