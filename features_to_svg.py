from shapely import polygons, get_type_id
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from get_svg_element import get_svg_element
import json

def features_to_svg(shape_data):
 content=''
 for f in shape_data[0]:
  j=f.ExportToJson()
  k=json.loads(j)
  geo_type=k['geometry']['type']
  print('geo type', geo_type, len(k['geometry']['coordinates']))
  feature_coords=k['geometry']['coordinates']
  fc=[]
  if geo_type=='MultiPolygon':
   fcs=feature_coords[0]
  if geo_type=='Polygon':
   fcs=feature_coords
  for fc in fcs:
   shapely_polygon=polygons(fc)
   d_path_value=get_svg_d_path(shapely_polygon)
   content+='<g transform-origin="center" transform="scale(1)">'
   content+='<path d="{0}" fill="red" stroke="green" />'.format(d_path_value)
   content+='</g>'
 return content