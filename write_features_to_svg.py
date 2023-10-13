from osgeo import ogr
from shapely import from_geojson,buffer,affinity, MultiPolygon, Polygon, LineString, MultiLineString
from get_svg_document import get_svg_document

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/roads.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]

# populate shape_objects with data from JSON call
def get_geo_data(layers, num):
 # 250240
 items_num=800
 shapes_json=[]
 for i in range(0,items_num):
  feature=layers[i]
  geojson=feature.ExportToJson(True)
  name=geojson['properties']['name']
  if(str(name)!='None'):
    print(name)
    shapes_json.append(geojson)
 return shapes_json

geo_data=get_geo_data(layers,10)

coords=[]
for s in geo_data:
 coords.append(s['geometry']['coordinates'])
multi_line_string = MultiLineString(coords)
scale_factor=700
mls_scaled=affinity.scale(multi_line_string,scale_factor,scale_factor)
mls_scaled_list=list(mls_scaled.geoms)

# loop through data and make shape objects, scale MultiLineString
def get_text_svg(geo_data,shapes):
 str=''
 for i in range(0,len(geo_data)):
  line_string=LineString(shapes[i])
  s='<text font-size="3" x="{}" y="{}" fill="black" stroke="none">{}</text>'
  str+=s.format(line_string.centroid.x,line_string.centroid.y,geo_data[i]['properties']['name'])

 return str

doc='' 
doc+=get_text_svg(geo_data,mls_scaled_list)
doc+=mls_scaled.svg(0.25,'black', 1.0)

f=open('generated/features_10_13_2023.svg', 'w')
f.write(get_svg_document(doc))