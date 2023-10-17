import json
from osgeo import ogr
from shapely import  affinity,from_geojson,MultiPolygon
from get_svg_document import get_svg_document

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)
sql="SELECT * FROM natural where type='park' limit 300"
layer=data_source.ExecuteSQL(sql)
print(layer.GetFeatureCount())
for feature in layer:
 print(feature.ExportToJson())
geo_data=[]
for feature in layer:
 geo_data.append(feature.ExportToJson(True))
polygons=[
 affinity.scale(from_geojson(json.dumps(gd)),3,3)
  for gd in geo_data]
multi_polygon=MultiPolygon(polygons)
multi_polygon_scaled=affinity.scale(multi_polygon,2000,-2000)
# create the document, write the file
doc=''
# doc+=multi_polygon_scaled.svg(1,'gray',0.5)
for i in range(0,len(geo_data)):
 shapely_polygon=multi_polygon_scaled.geoms[i]
 doc+=shapely_polygon.svg(1,'blue',0.5)
 svg_text='<text font-size="{}" x="{}" y="{}" fill="{}" stroke="none">{}</text>'
 doc+=svg_text.format(
  7,
  shapely_polygon.centroid.x, shapely_polygon.centroid.y,
  'purple',
  geo_data[i]['properties']['name'])

j=open('generated/features_10_17_2023.svg', 'w')
j.write(get_svg_document(doc))