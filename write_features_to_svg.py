from osgeo import ogr
from Features import Features
from SVGTag import SVGTag

# set the layer that will be used as an argument to the Features class
data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(300)
layer=data_source.ExecuteSQL(sql)
# set up the two main clases Features and SVGTag
features=Features(layer)
features.print_info()
svg_tag=SVGTag()
# build the SVGTag
for i in range(0,len(features.data)):
 svg_tag.set_polygon(features.scaled_group.geoms[i].svg())
 svg_tag.set_text_element(
  features.data[i]['properties']['name'],
  features.scaled_group.geoms[i].centroid.x,features.scaled_group.geoms[i].centroid.y,
  7
 )
# render the SVGTag
j=open('generated/features_10_31_2023.svg', 'w')
j.write(svg_tag.render())