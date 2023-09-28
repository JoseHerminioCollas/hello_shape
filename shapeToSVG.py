import re
from osgeo import ogr
import json
from shapely import polygons

def pointSVG(cx, cy, color='blue', radius=10):
 z = '<circle r="{3}" cx="{0}" cy="{1}" fill="{2}" stroke="none" />'.format(cx, cy, color, radius)
 return z

def polygonSVG(polygon):
 return ' <polygon points="{0}" fill="red" stroke="black" />'.format(polygon)

def writeDebug(content):
 f=open('debug.json','w')
 f.write(content)

def writeSVG(d):
 content='<path d="{0}" fill="red" stroke="green" />'.format(d)
 openTag='<svg viewBox="-100 -100 100 100" width="200" height="200">'
 bGTag='<rect width="20" height="200" x="-20" y="-20" fill="blue" />'
 openG='<g transform-origin="center" transform="scale(1)">'
 f=open('countries.svg', 'w')
 f.write(openTag)
 f.write(bGTag)
 f.write(openG)
 f.write(content)
 f.write('</g></svg>')

def getSVGPathD(shapelyPolygon):
 pSVG=shapelyPolygon.svg()
 regexpA=re.compile(r'd="(.*)"')
 m=regexpA.search(pSVG)
 return m.groups()[0]

def getFeatureCoords(feature):
 featureJSON=feature.ExportToJson()
 featureObj=json.loads(featureJSON)
 # has only one entry because it is a polygon
 return featureObj['geometry']['coordinates'][0]

dataPath="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
data=ogr.Open(dataPath)

feature=data[0][3]
featureCoords=getFeatureCoords(feature)
shapelyPolygon=polygons(featureCoords)
pathValue=getSVGPathD(shapelyPolygon)

writeSVG(pathValue)