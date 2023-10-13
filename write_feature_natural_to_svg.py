import json
from osgeo import ogr
from shapely import  affinity,from_geojson
from get_svg_document import get_svg_document
from get_geo_data import get_geo_data
from get_text_svg_element import get_text_svg_element

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]
# OGR features to geo json Python data
geo_data=get_geo_data(layers,1000)

doc=''
# write text elements to label the areas
for i in range(0,len(geo_data)):
 el=from_geojson(json.dumps(geo_data[i]))
 el2=affinity.scale(el,100000,100000)
 doc+=get_text_svg_element(
  el2.centroid.x,
  el2.centroid.y,
  geo_data[i]['properties']['name']
  )

f=open('generated/features_10_13_b_2023.svg', 'w')
f.write(get_svg_document(doc))