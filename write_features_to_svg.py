from osgeo import ogr
from features_to_svg import features_to_svg

data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
shape_data=ogr.Open(data_path)

content='<svg viewBox="-100 -100 300 200" width="300" height="200">'
content+='<rect width="299" height="99" x="-100" y="0" fill="peru" />'
content+=features_to_svg(shape_data)
content+='</svg>'

f=open('generated/features_1.svg', 'w')
f.write(content)