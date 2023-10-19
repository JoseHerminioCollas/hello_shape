import json
from osgeo import ogr
from shapely import  affinity,from_geojson,MultiPolygon
from get_svg_document import get_svg_document
data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)
item_scale=3
group_scale=2000
limit=100
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(limit)
layer=data_source.ExecuteSQL(sql)
print(layer.GetName())
features=[]
class feat():
 print(3)
 def a():
  print(3)
geo_data_features=[feature.ExportToJson(True) for feature in layer]
[print('z', geo_data_features[i]) for i in range(len(geo_data_features))]
# for feature in layer:
#  geo_data_features.append(feature.ExportToJson(True))    
polygons=[
 affinity.scale(from_geojson(json.dumps(gd)),item_scale,item_scale)
  for gd in geo_data_features]
multi_polygon=MultiPolygon(polygons)
multi_polygon_scaled=affinity.scale(multi_polygon,group_scale,-group_scale)
# create the document, write the file
doc=''
# doc+=affinity.scale(from_geojson(gr.ExportToJson()),1000,-1000).svg(1,'blue',0.5)
# doc+=multi_polygon_scaled.svg(1,'gray',0.5)
svg_text='<text font-size="{}" x="{}" y="{}" fill="{}" stroke="none">{}</text>'
for i in range(0,len(geo_data_features)):
 shapely_polygon=multi_polygon_scaled.geoms[i]
 doc+=shapely_polygon.svg(0.1,'red',0.5)
 doc+=svg_text.format(
  3,
  shapely_polygon.centroid.x, shapely_polygon.centroid.y,
  'rgba(3,3,3,0.5)',
  geo_data_features[i]['properties']['name'])

j=open('generated/features_10_19_2023.svg', 'w')
j.write(get_svg_document(doc))