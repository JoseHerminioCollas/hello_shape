from osgeo import ogr
from shapely import from_geojson,buffer,affinity, MultiPolygon, Polygon, LineString, MultiLineString
from shape_to_svg import shape_to_svg
from get_svg_document import get_svg_document

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/roads.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]

# populate shape_objects with data from JSON call
def get_shapes_json(layers, num):
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
shape_json=get_shapes_json(layers,10)

# shape objects scaled
# def get_scaled_MultiString():
#  multi = MultiLineString(shape_json)
#  scale_factor=700
#  m_scaled=affinity.scale(multi,scale_factor,scale_factor)
#  return m_scaled

doc='' 
coords=[]
for s in shape_json:
#  print(s)
 coords.append(s['geometry']['coordinates'])
multi = MultiLineString(coords)
scale_factor=700
m_scaled=affinity.scale(multi,scale_factor,scale_factor)
scaled_list=list(m_scaled.geoms)
doc+=m_scaled.svg(0.25,'black', 1.0)

# loop through data and make shape objects, scale MultiLineString
for j in range(0,len(shape_json)):
 ls=LineString(scaled_list[j])
 str='<text font-size="3" x="{}" y="{}" fill="black" stroke="none">{}</text>'
 doc+=str.format(ls.centroid.x,ls.centroid.y,shape_json[j]['properties']['name'])

f=open('generated/features_10_12_2023.svg', 'w')
f.write(get_svg_document(doc))