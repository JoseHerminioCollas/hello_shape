from shapely import polygons, get_type_id
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from get_svg_element import get_svg_element
import json

def features_to_svg(shape_data):
 content=''
 for i in range(0,200):
  f=shape_data[0][i]
  jse = f.ExportToJson(True)
  props=jse['properties']
  idd=jse['properties']['ISO_N3']
  if True:
   geo_type=jse['geometry']['type']
   feature_coords=jse['geometry']['coordinates']
   for fc in feature_coords:
     print('333',len(fc))
     if geo_type=='MultiPolygon':
      fcs2=fc[0]
      print('xxx', len(feature_coords))
     if geo_type=='Polygon':
      fcs2=fc
     
     shapely_polygon=polygons(fcs2)
     d_path_value=get_svg_d_path(shapely_polygon)
     content+='<g transform-origin="center" transform="scale(1)">'
     content+='<path d="{0}" fill="red" stroke="green" />'.format(d_path_value)
     content+='</g>'
 return content