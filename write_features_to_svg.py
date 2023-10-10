from osgeo import ogr
from shapely import from_geojson,buffer,affinity, MultiPolygon, Polygon
from shape_to_svg import shape_to_svg
from get_svg_document import get_svg_document

data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/buildings.shp'
data_source=ogr.Open(data_path)
layers=data_source[0]
polygons=[]
for i in range(0,20):
 feature=layers[i]
 name=feature.GetField('NAME')
 print('name: ',name)
 geojson=feature.ExportToJson()
 shape_one=from_geojson(geojson)
 shape_two=affinity.scale(shape_one, 20,20)
 polygons.append(shape_two)

doc=''
multi_polygon = MultiPolygon(polygons)
m_p_scaled=affinity.scale(multi_polygon,1500,1500)
m_p_list=list(m_p_scaled.geoms)
for m_p in m_p_list:
 b=Polygon(m_p)
 str='<text size="44" x="{}" y="{}" fill="black" stroke="red">XXX</text>'
 doc+=str.format(b.centroid.x,b.centroid.y)

doc+=m_p_scaled.svg(1,'green', 1)
svg_document=get_svg_document(doc)

f=open('generated/featuresx.svg', 'w')
f.write(svg_document)