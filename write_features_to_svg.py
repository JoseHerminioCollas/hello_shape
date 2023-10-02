from osgeo import ogr
from features_to_svg import features_to_svg

data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
shape_data=ogr.Open(data_path)
content='<svg viewBox="-200 150 400 300" width="400" height="300" stroke="gray" stroke-width="0.5" transform="scale(1,-1) translate(0, 0)">'
content+='<rect width="100" height="99" x="-100" y="0" fill="blue" stoke-width="0.25"/>'
content+='<rect width="100" height="99" x="-0" y="0" fill="green"  stoke-width="0.25"/>'
content+='<rect width="100" height="99" x="100" y="-100" fill="red"  stoke-width="0.25"/>'
content+='<rect width="100" height="99" x="-200" y="-100" fill="yellow"  stoke-width="0.25"/>'
content+=features_to_svg(shape_data)
content+='</svg>'

f=open('generated/features_1.svg', 'w')
f.write(content)