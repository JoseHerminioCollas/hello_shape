import re
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
p=re.compile(r'd="(.*)"')
m=p.search(pSVG)
pathValue=m.groups()[0]
print(pathValue)
content='<path d="{0}" fill="red" stroke="blue" />'.format(pathValue)
debugStr=debugStr+a
openTag='<svg viewBox="-100 -100 100 100" width="200" height="200">'
bGTag='<rect width="20" height="200" x="-20" y="-20" fill="red" />'
openG='<g transform-origin="center" transform="scale(1)">'
f=open('countries.svg', 'w')
f.write(openTag)
f.write(bGTag)
f.write(openG)
f.write(content)
f.write('</g></svg>')

f=open('debug.json','w')
f.write(debugStr)