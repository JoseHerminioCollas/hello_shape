from osgeo import ogr
from shapely import from_geojson,buffer,affinity, MultiPolygon, Polygon
from shape_to_svg import shape_to_svg
from get_svg_document import get_svg_document

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/buildings.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]
polygons=[]
items_num=1100
for i in range(0,items_num):
 feature=layers[i]
 name=feature.GetField('NAME')
#  print('name: ',name)
 geojson=feature.ExportToJson()
 shape_one=from_geojson(geojson)
 shape_two=affinity.scale(shape_one,3,3)
 polygons.append(shape_two)

doc=''
multi_polygon = MultiPolygon(polygons)
m_p_scaled=affinity.scale(multi_polygon,2000,2000)
m_p_list=list(m_p_scaled.geoms)
doc+=m_p_scaled.svg(1,'blue', 1)

for j in range(0,items_num):
 poly=Polygon(m_p_list[j])
 poly_info=layers[j].ExportToJson(True)
 print('xx',poly_info['properties']['name'])
 str='<text font-size="9" x="{}" y="{}" fill="black" stroke="none">{}</text>'
#  doc+=str.format(poly.centroid.x,poly.centroid.y,poly_info['properties']['name'])

svg_document=get_svg_document(doc)

f=open('generated/featuresx.svg', 'w')
f.write(svg_document)