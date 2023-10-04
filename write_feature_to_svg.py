from osgeo import ogr
from shapely import from_wkb, from_geojson, buffer
from feature_to_svg import feature_to_svg
from get_svg_document import get_svg_document
from shape_to_svg import shape_to_svg

data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
countries_data=ogr.Open(data_path)
countries_layers=countries_data[0]

# get features
feature=countries_layers[3]
feature2=countries_layers[1]

# make shape objects from features
geojson = feature2.ExportToJson()
shape_one=from_geojson(geojson)
shape_two=buffer(shape_one, 2,1)

# generate svg from features and shapes
content=''
content+=shape_to_svg(shape_two, 'blue')
content+=shape_to_svg(shape_one, 'green')
content+=feature_to_svg(feature)
content+=feature_to_svg(feature2)
svg_document=get_svg_document(content)

file_name='generated/feature.svg'
f=open(file_name, 'w')
f.write(svg_document)
