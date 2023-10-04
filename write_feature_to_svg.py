from osgeo import ogr
from shapely import from_wkb, from_geojson
import re
 
def feature_to_svg(feature):
    wkb = feature.ExportToJson()
    shapely_object=from_geojson(wkb)
    path_tag=re.sub(r'stroke="#\d+" ', '', shapely_object.svg(0.25, 'blue', 1.0))
    return path_tag

def get_svg_document(inner_contents):
    content='<svg viewBox="-200 150 400 300" width="400" height="300" stroke="rgba(3,3,3,0.0)" stroke-width="0.0" transform="scale(1,-1) translate(0, 0)">'
    content+='<rect width="100" height="99" x="-100" y="0" fill="blue" stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="-0" y="0" fill="green"  stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="100" y="-100" fill="red"  stoke-width="0.25"/>'
    content+='<rect width="100" height="99" x="-200" y="-100" fill="yellow"  stoke-width="0.25"/>'
    content+=inner_contents
    content+='</svg>'
    return content

data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
countries_data=ogr.Open(data_path)

feature=countries_data[0][3]
feature_svg=feature_to_svg(feature)
svg_document=get_svg_document(feature_svg)

f=open('generated/feature.svg', 'w')
f.write(svg_document)