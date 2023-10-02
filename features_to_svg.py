from shapely import polygons, from_geojson, buffer, Point
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from get_svg_element import get_svg_element
import re
 
def features_to_svg(shape_data):
 content=''
#  range(0,len(shape_data[0]))
 for i in range(0,10):
  feature=shape_data[0][i]
  print(feature.GetField('ISO_N3'))
  jse = feature.ExportToJson()
  shp=from_geojson(jse)  
  shp2=buffer(shp,2,1)
  color='rgba({},{},{},1.0)'.format(i,i,i)
  path_tag=re.sub(r'stroke="#\d+" ', '', shp.svg(0.25, 'green', 1.0))
  path_tag2=re.sub(r'stroke="#\d+" ', '', shp2.svg(0.25, 'yellow', 1.0))
  content+=path_tag2
  content+=path_tag
 return content