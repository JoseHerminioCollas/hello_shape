import json
from osgeo import ogr
from shapely import  affinity,from_geojson,MultiPolygon
from get_svg_document import get_svg_document

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)
gr=ogr.CreateGeometryFromWkt('POLYGON ((-3.8 40,-3.4 40.5,-3 40.5,-3 40.25,-3.8 40))')
print(gr)
# ,[(0,0),(0,1),(1,1),(1,0)] (-4.0699641, -3.2300143, 40.170042, 40.6499669)
sql="SELECT * FROM natural where type='park' limit 1300"
layer=data_source.ExecuteSQL(sql,gr )
e=layer.GetExtent()
print(e)
# one_data_source_for_all ????
geo_data_features=[]
for feature in layer:
#  print(feature.geometry())
 geo_data_features.append(feature.ExportToJson(True))    

polygons=[
 affinity.scale(from_geojson(json.dumps(gd)),3,3)
  for gd in geo_data_features]
multi_polygon=MultiPolygon(polygons)
multi_polygon_scaled=affinity.scale(multi_polygon,200,-200)

# create the document, write the file
doc=''
doc+=affinity.scale(from_geojson(gr.ExportToJson()),200,200).svg(1,'blue',0.5)
# doc+=multi_polygon_scaled.svg(1,'gray',0.5)
svg_text='<text font-size="{}" x="{}" y="{}" fill="{}" stroke="none">{}</text>'
for i in range(0,len(geo_data_features)):
 shapely_polygon=multi_polygon_scaled.geoms[i]
 doc+=shapely_polygon.svg(1,'red',0.5)
#  doc+=svg_text.format(
#   11,
#   shapely_polygon.centroid.x, shapely_polygon.centroid.y,
#   'purple',
#   geo_data_features[i]['properties']['name'])

j=open('generated/features_10_18_2023.svg', 'w')
j.write(get_svg_document(doc))