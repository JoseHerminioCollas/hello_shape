from osgeo import ogr
import json
from shapely import polygons, get_type_id

def pointSVG(cx, cy, color='blue', radius=10):
 z = '<circle r="{3}" cx="{0}" cy="{1}" fill="{2}" stroke="none" />'.format(cx, cy, color, radius)
 return z

def polygonSVG(polygon):
 return ' <polygon points="{0}" fill="red" stroke="black" />'.format(polygon)

dataPath="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
data=ogr.Open(dataPath)

content=pointSVG(10,10)
debugStr=''
feature=data[0][3]
a=feature.ExportToJson()
b=json.loads(a)
# has only one entry because it is a polygon
c=b['geometry']['coordinates'][0]
p=polygons(c)

pSVG=p.svg()
content=pSVG
debugStr=debugStr+a
openTag='<svg viewBox="-100 -100 200 200" width="500" height="500">'
openG='<g transform-origin="center" transform="scale(1)">'
bGTag='<rect width="200" height="200" fill="black" />'
f=open('countries.svg', 'w')
# viewBox="-300 -200 600 400"
#  transform="translate(150,75) scale(2)"
f.write(openTag)
f.write(bGTag)
f.write(openG)
f.write(content)
f.write('</g></svg>')

f=open('debug.json','w')
f.write(debugStr)