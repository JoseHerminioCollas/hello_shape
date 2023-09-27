from osgeo import ogr
import json

def pointSVG(cx, cy, color='blue', radius=10):
 z = '<circle r="{3}" cx="{0}" cy="{1}" fill="{2}" stroke="none" />'.format(cx, cy, color, radius)
 return z

dataPath="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
data=ogr.Open(dataPath)

content=pointSVG(10,10)
debugStr=''
feature=data[0][3]
a=feature.ExportToJson()
b=json.loads(a)
c=b['geometry']['coordinates']


print(b['geometry']['type'])
debugStr=debugStr+a

f=open('countries.svg', 'w')
f.write('<svg width="140" height="140" fill="black" stroke="black">')
f.write(content)
f.write('</svg>')

f=open('debug.json','w')
f.write(debugStr)