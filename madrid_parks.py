from osgeo import ogr
from Features import Features
from SVGTag import SVGTag

def madrid_parks(data_path,sql,destination_path):
 data_source=ogr.Open(data_path)
 layer=data_source.ExecuteSQL(sql)
 features=Features(layer)
 svg_tag=SVGTag()
 for i in range(0,len(features.data)):
  svg_tag.set_polygon(features.scaled_group.geoms[i].svg())
  svg_tag.set_text_element(
   features.data[i]['properties']['name'],
   features.scaled_group.geoms[i].centroid.x, features.scaled_group.geoms[i].centroid.y,
   3
  )
 j=open(destination_path, 'w')
 j.write(svg_tag.render())
