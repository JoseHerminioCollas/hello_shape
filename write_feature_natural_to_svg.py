import json
from osgeo import ogr
from shapely import  affinity,from_geojson,MultiPolygon,get_dimensions
from get_svg_document import get_svg_document
from Features import Features
from get_svg import get_svg

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)

limit=1000
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(limit)
layer=data_source.ExecuteSQL(sql)

features=Features(layer)
for p in features.scaled_group.geoms:
 print( p )

doc=[
 get_svg(features.scaled_group.geoms[i],features.data[i])
  for i in range(0,len(features.data))]

j=open('generated/features_10_30_2023.svg', 'w')
j.write(get_svg_document(''.join(doc)))