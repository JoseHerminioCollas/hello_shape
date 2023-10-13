import json
from osgeo import ogr
from shapely import  affinity,from_geojson, MultiPolygon
from get_svg_document import get_svg_document
from get_geo_data import get_geo_data
from get_text_svg_element import get_text_svg_element

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/landuse.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]
# OGR features to geo json Python data
geo_data=get_geo_data(layers,1000)

shape_num=len(geo_data)
# shapely_objects=[]
# for i in range(0,shape_num):
#  el=from_geojson(json.dumps(geo_data[i]))
#  el2=affinity.scale(el,1,1)
#  shapely_objects.append(el2)

def b(k):
 el=from_geojson(json.dumps(geo_data[k]))
 el2=affinity.scale(el,1,1)
 return el2
 
a=[b(k) for k in range(shape_num)]

mp=MultiPolygon(a)
mp2=affinity.scale(mp,2000,2000)

doc=''
doc+=mp2.svg(1,'red',1.0)
# write text
for i in range(0,shape_num):
 el2=mp2.geoms[i]
 doc+=get_text_svg_element(
  el2.centroid.x,
  el2.centroid.y,
  geo_data[i]['properties']['name'],
  4
  )

f=open('generated/features_10_13_c_2023.svg', 'w')
f.write(get_svg_document(doc))