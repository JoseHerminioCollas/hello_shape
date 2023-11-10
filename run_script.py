from madrid_parks import madrid_parks
from shapely import from_wkt
from osgeo import ogr

data_path = 'data/Madrid-shp/shape/natural.shp'
destination_path = '__generated/madrid_parks_11_9.svg'
# feature.GetGeometryRef()
wkt = "POLYGON ((1162440.5712740074 672081.4332727483, 1162440.5712740074 647105.5431482664, 1195279.2416228633 647105.5431482664, 1195279.2416228633 672081.4332727483, 1162440.5712740074 672081.4332727483))"
wkt2 = "POLYGON ((-3.25 40.170, -3.2 40.6 ))"
wkt3 = "POLYGON ((-3.25 40.17, -3.2 40.17, -3.2 40.6, -3.25 40.6, -3.25 40.17))"
poly = ogr.CreateGeometryFromWkt(wkt3)
print ("Area = %d" % poly.GetArea())
sql = "SELECT * FROM natural where type='park' and name is not null limit {}".format(300)
data_source = ogr.Open(data_path)
layer = data_source.ExecuteSQL(sql,poly)
print(len(layer))
svg_tag=madrid_parks(layer, destination_path)
svg_tag.set_polygon(from_wkt(wkt3).svg())
j = open(destination_path, 'w')
j.write(svg_tag.render())
