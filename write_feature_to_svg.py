from osgeo import ogr
from feature_to_svg import feature_to_svg

data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
shape_data=ogr.Open(data_path)

def svg_document(inner_contents):
    content='<svg viewBox="-200 150 400 300" width="400" height="300" stroke="rgba(3,3,3,0.0)" stroke-width="0.0" transform="scale(1,-1) translate(0, 0)">'
    content+='<rect width="100" height="99" x="-100" y="0" fill="blue" stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="-0" y="0" fill="green"  stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="100" y="-100" fill="red"  stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="-200" y="-100" fill="yellow"  stoke-width="0.25"/>'
    content+=inner_contents
    content+='</svg>'
    return content

c=''

feature_svg=feature_to_svg(feature)

svgDoc=svg_document(feature_to_svg)

f=open('generated/feature.svg', 'w')
f.write(c)