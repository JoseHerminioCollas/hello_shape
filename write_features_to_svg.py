from osgeo import ogr
from shapely import  affinity,MultiLineString
from get_svg_document import get_svg_document
from get_geo_data import get_geo_data
from get_text_svg import get_text_svg

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/roads.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]
# OGR features to geo json Python data
geo_data=get_geo_data(layers,3000)
# scale with a MultiLineString
coords=[]
for s in geo_data:
 coords.append(s['geometry']['coordinates'])
multi_line_string = MultiLineString(coords)
scale_factor=700
mls_scaled=affinity.scale(multi_line_string,scale_factor,scale_factor)
mls_scaled_list=list(mls_scaled.geoms)
# write to the doc object and write the file
doc=get_text_svg(geo_data,mls_scaled_list)
doc+=mls_scaled.svg(0.25,'black', 1.0)
f=open('generated/features_10_13_2023.svg', 'w')
f.write(get_svg_document(doc))