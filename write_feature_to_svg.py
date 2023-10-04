from osgeo import ogr
from shapely import from_wkb, from_geojson, buffer
from get_svg_document import get_svg_document
from shape_to_svg import shape_to_svg

data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
countries_data=ogr.Open(data_path)

feature=countries_data[0][3]

geojson = feature.ExportToJson()
shape_one=from_geojson(geojson)
shape_two=buffer(shape_one,2,1)

shape_feature_svg=shape_to_svg(shape_one, 'red')
shape_feature_svg_two=shape_to_svg(shape_two, 'blue')
svg_document=get_svg_document(shape_feature_svg_two+shape_feature_svg)

f=open('generated/feature.svg', 'w')
f.write(svg_document)

print('script complete:', feature.GetField('ISO_N3'))
