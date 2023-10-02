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
  if idd=='840':
#    print('usa', props)
#    print(jse['geometry'])
#   print(idd)
#   for i in range(f.GetFieldCount()):
#    print('xxxx', f.GetFieldDefnRef(i).GetName())
#    print('xxxx', f.GetFieldDefnRef(i).GetType())
#    print(f.GetGeomFieldCount())
#   for i in range(f.GetGeomFieldCount()):
#    print('a', f.GetGeomFieldDefnRef(i).GetName())
#    print(f.GetGeomFieldDefn(i).GetType())
# GetGeomFieldDefn(i).GetType()
#   j=f.ExportToJson()
#   k=json.loads(j)
   geo_type=jse['geometry']['type']
#   print('geo type', geo_type, len(k['geometry']['coordinates']))
   feature_coords=jse['geometry']['coordinates']
#   fc=[]
   if geo_type=='MultiPolygon':
    fcs=feature_coords
    print('xxx', len(feature_coords))
   if geo_type=='Polygon':
    fcs=feature_coords
   for fc in fcs:
     print('333',len(fc))
     shapely_polygon=polygons(fc[0])
     d_path_value=get_svg_d_path(shapely_polygon)
     content+='<g transform-origin="center" transform="scale(1)">'
     content+='<path d="{0}" fill="red" stroke="green" />'.format(d_path_value)
     content+='</g>'
 return content