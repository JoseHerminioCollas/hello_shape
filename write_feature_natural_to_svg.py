import json
from osgeo import ogr
from Features import Features

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)

limit=50
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(limit)
layer=data_source.ExecuteSQL(sql)

features=Features(layer)
features.print_info()
class SVGTag():
 name='SVGTag'
 def __init__(self):
  self.doc=''
 def render(self):
  svg_doc = '<svg viewBox="-300 -300 600 600" width="600" height="600" stroke="green" stroke-width="1">'
  svg_doc += self.doc
  svg_doc += '</svg>'
  return svg_doc
 def set_text_element(self,name,x,y,font_size=1,color='rgba(3,3,113,0.5)'):
  svg_text='<text font-size="{}" x="{}" y="{}" fill="{}" stroke="none">{}</text>'
  self.doc+=svg_text.format(font_size,x,y,color,name)
 def set_polygon(self,str):
  self.doc+=str
  return True

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