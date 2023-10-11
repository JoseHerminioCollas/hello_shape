from osgeo import ogr
from shapely import from_geojson,buffer,affinity, MultiPolygon, Polygon, LineString, MultiLineString
from shape_to_svg import shape_to_svg
from get_svg_document import get_svg_document

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/roads.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]
shape_objects=[]
items_num=5900
doc=''
# populate shape_objects with data from JSON call
geo=[]
for i in range(0,items_num):
 feature=layers[i]
 geojson=feature.ExportToJson(True)
 name=geojson['properties']['name']
 if(str(name)!='None'):
  print(name)
  shape_objects.append(geojson)
  geo.append(geojson['geometry']['coordinates'])
multi = MultiLineString(geo)
scale_factor=2000
m_scaled=affinity.scale(multi,scale_factor,scale_factor)
scaled_list=list(m_scaled.geoms)
doc+=m_scaled.svg(1,'blue', 1)
# loop through data and make shape objects, scale MultiLineString
for j in range(0,len(shape_objects)):
 ls=LineString(scaled_list[j])
#  print(ls)
 str='<text font-size="3" x="{}" y="{}" fill="black" stroke="none">{}</text>'
 doc+=str.format(ls.centroid.x,ls.centroid.y,shape_objects[j]['properties']['name'])
svg_document=get_svg_document(doc)
f=open('generated/features_10_11_2023.svg', 'w')
f.write(svg_document)