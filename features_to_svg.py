from shapely import polygons, from_geojson, buffer, Point
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from get_svg_element import get_svg_element
import json
import re

def get_path_d(svg_path_tag):
 regexpA=re.compile(r'd="(.*)"')
 m=regexpA.search(svg_path_tag)
 return m.groups()[0]
 
def features_to_svg(shape_data):
 content=''
#  range(0,len(shape_data[0]))
 for i in range(0,100):
  feature=shape_data[0][i]
  print(feature.GetField('ISO_N3'))
  jse = feature.ExportToJson()
  shp=from_geojson(jse)  
  shp2=buffer(shp,2,1)
  color='rgba({},{},{},1.0)'.format(i,i,i)
  svg='<path d="{}" fill="red" />'.format(get_path_d(shp.svg()))
  svg2='<path d="{}" fill="{}"/>'.format(get_path_d(shp2.svg()), color)
  content+=svg
  content+=svg2
 return content