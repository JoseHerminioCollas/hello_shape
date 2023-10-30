import json
from osgeo import ogr
from shapely import  affinity,from_geojson,MultiPolygon
from get_svg_document import get_svg_document
from Features import Features
from get_svg import get_svg

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)

limit=100
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(limit)
layer=data_source.ExecuteSQL(sql)

features=Features(layer)
for f in features.scaled:
 print('f')

for p in features.poygons:
 print(p)
item_scale=1
group_scale=2000
# features.polygons=[
#  affinity.scale(from_geojson(json.dumps(gd)),item_scale,item_scale)
#   for gd in features.data]
# features.multi_polygon=MultiPolygon(features.polygons)
# features.multi_polygon_scaled=affinity.scale(features.multi_polygon,group_scale,-group_scale)

# doc=[
#  get_svg(features.multi_polygon_scaled.geoms[i],features.data[i])
#   for i in range(0,len(features.data))]

# j=open('generated/features_10_19_2023.svg', 'w')
# j.write(get_svg_document(''.join(doc)))