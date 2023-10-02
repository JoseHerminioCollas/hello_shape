from shapely import polygons, from_geojson
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from get_svg_element import get_svg_element
import json
import re

def features_to_svg(shape_data):
 content=''
 for i in range(0,len(shape_data[0])):
  feature=shape_data[0][i]
  print(feature.GetField('ISO_N3'))
  jse = feature.ExportToJson()
  shp=from_geojson(jse)  
  color='rgba({},{},{},1.0)'.format(i,i,i)
  svg=shp.svg(0.1,color, 1.0)
  svg2=re.sub('stroke="#\d+"', '', svg)
  content+=svg2
 return content