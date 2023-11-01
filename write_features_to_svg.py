from osgeo import ogr
from Features import Features
from SVGTag import SVGTag
def madrid_parks(data_path,sql):
 data_source=ogr.Open(data_path)
 layer=data_source.ExecuteSQL(sql)
 features=Features(layer)
 features.print_info()
 svg_tag=SVGTag()
 for i in range(0,len(features.data)):
  svg_tag.set_polygon(features.scaled_group.geoms[i].svg())
  svg_tag.set_text_element(
   features.data[i]['properties']['name'],
   features.scaled_group.geoms[i].centroid.x, features.scaled_group.geoms[i].centroid.y,
   3
  )
 j=open('generated/madrid_parks_2023_11_1.svg', 'w')
 j.write(svg_tag.render())

calls=[
{
 'path':
  'data/Madrid-shp/shape/natural.shp',
 'sql':
  "SELECT * FROM natural where type='park' and name is not null limit {}"
   .format(60),
 'script':madrid_parks
}]
for i in range(0,len(calls)):
 print(calls[i])
 path=calls[i]['path']
 sql=calls[i]['sql']
 calls[i]['script'](path,sql)
