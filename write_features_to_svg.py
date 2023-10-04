from osgeo import ogr
from shapely import from_geojson, buffer
from shape_to_svg import shape_to_svg
from get_svg_document import get_svg_document

data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
countries_data=ogr.Open(data_path)

countries_layer=countries_data[0]
c=''
for i in range(0,100):
 feature=countries_layer[i]
 name=feature.GetField('NAME')
 print(name)
 geojson = feature.ExportToJson()
 shape_one=from_geojson(geojson)
 shape_two=buffer(shape_one,2,1)
 shape_feature_svg=shape_to_svg(shape_one, 'red')
 shape_feature_svg_two=shape_to_svg(shape_two, 'blue')
 c+=shape_feature_svg_two+shape_feature_svg

svg_document=get_svg_document(c)

f=open('generated/features.svg', 'w')
f.write(svg_document)