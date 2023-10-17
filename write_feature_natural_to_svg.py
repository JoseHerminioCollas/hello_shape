import json
from osgeo import ogr
from shapely import  affinity,from_geojson,MultiPolygon
from get_svg_document import get_svg_document
from get_text_svg_element import get_text_svg_element

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/buildings.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]
geo_data=[]
print(len(layers))
feature_count=500
for f in range(0,feature_count):
 geo_data.append(layers[f].ExportToJson(True))
polygons=[from_geojson(json.dumps(geo_data[k])) for k in range(0,feature_count)]
multi_polygon=MultiPolygon(polygons)
multi_polygon_scaled=affinity.scale(multi_polygon,2000,-2000)
# create the document, write the file
doc=''
doc+=multi_polygon_scaled.svg(1,'gray',0.5)
for i in range(0,feature_count):
 shapely_polygon=multi_polygon_scaled.geoms[i]
 doc+=get_text_svg_element(
  shapely_polygon.centroid.x,shapely_polygon.centroid.y,
  geo_data[i]['properties']['name'], 4)

f=open('generated/features_10_17_2023.svg', 'w')
f.write(get_svg_document(doc))