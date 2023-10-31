import json
from osgeo import ogr
from get_svg_document import get_svg_document
from Features import Features
# from get_svg import get_svg

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.shp'
data_source=ogr.Open(data_path)

limit=50
sql="SELECT * FROM natural where type='park' and name is not null limit {}".format(limit)
layer=data_source.ExecuteSQL(sql)

features=Features(layer)
features.print_info()
def get_svg_document(inner_contents):
 content = '<svg viewBox="-300 -300 600 600" width="600" height="600" stroke="green" stroke-width="1">'
 content += '<rect x="0" y="0" width="290" height="290" fill="green" />'
 content += inner_contents
 content += '</svg>'
 return content
def get_svg_text_element(name,x,y,font_size=1,color='rgba(3,3,3,0.5)'):
 svg_text='<text font-size="{}" x="{}" y="{}" fill="{}" stroke="none">{}</text>'
 return svg_text.format(font_size,x,y,color,name)
doc=''
for i in range(0,len(features.data)):
 doc+=features.scaled_group.geoms[i].svg()
 doc+=get_svg_text_element(
  features.data[i]['properties']['name'],
  features.scaled_group.geoms[i].centroid.x,features.scaled_group.geoms[i].centroid.y,
  7
 )
svg_doc=get_svg_document(doc)

j=open('generated/features_10_31_2023.svg', 'w')
j.write(svg_doc)