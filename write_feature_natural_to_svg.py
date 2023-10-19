import json
from osgeo import ogr
from shapely import  affinity,from_geojson,MultiPolygon
from get_svg_document import get_svg_document
from get_svg_text_element import get_svg_text_element
data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)
item_scale=1
group_scale=2000
limit=1000
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(limit)
layer=data_source.ExecuteSQL(sql)
class Features:
 def __init__(self, layer):
  self.data=[feature.ExportToJson(True) for feature in layer]
 polygons=[]
 multi_polygon=[]
 multi_polygon_scaled=[]
features=Features(layer)
features.polygons=[
 affinity.scale(from_geojson(json.dumps(gd)),item_scale,item_scale)
  for gd in features.data]
features.multi_polygon=MultiPolygon(features.polygons)
features.multi_polygon_scaled=affinity.scale(features.multi_polygon,group_scale,-group_scale)
def get_svg(name,x,y,poly):
 svg=poly
 svg+=get_svg_text_element(name,x,y)
 return svg
doc=[
 get_svg(
  features.data[i]['properties']['name'],
  features.multi_polygon_scaled.geoms[i].centroid.x,
  features.multi_polygon_scaled.geoms[i].centroid.y,
  features.multi_polygon_scaled.geoms[i].svg()
 ) 
  for i in range(0,len(features.data))]

j=open('generated/features_10_19_2023.svg', 'w')
j.write(get_svg_document(''.join(doc)))