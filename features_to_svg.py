from shapely import polygons, from_geojson
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from get_svg_element import get_svg_element
import json

def features_to_svg(shape_data):
 content=''
 for i in range(0,200):
  print(i)
  feature=shape_data[0][i]
  jse = feature.ExportToJson()
#   make a shapely object
  shp=from_geojson(jse)  
  svg=shp.svg()
  content+=svg
  print('svg',svg)
  print(feature.GetField('ISO_N3'))
 return content