import json
from osgeo import ogr
from Features import Features
from SVGTag import SVGTag

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)

limit=150
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(limit)
layer=data_source.ExecuteSQL(sql)

features=Features(layer)
svg_tag=SVGTag()

for i in range(0,len(features.data)):
 svg_tag.set_polygon(features.scaled_group.geoms[i].svg())
 svg_tag.set_text_element(
  features.data[i]['properties']['name'],
  features.scaled_group.geoms[i].centroid.x,features.scaled_group.geoms[i].centroid.y,
  7
 )

j=open('generated/features_10_31_2023.svg', 'w')
j.write(svg_tag.render())