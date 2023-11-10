from madrid_parks import madrid_parks
from shapely import from_wkt, affinity
from osgeo import ogr

item_scale = 1
group_scale = 900
limit=3000
data_path = 'data/Madrid-shp/shape/natural.shp'
destination_path = '__generated/madrid_parks_11_10.svg'
wkt_spatial_filter = "POLYGON ((-3.5 40.17, -3.2 40.17, -3.2 40.6, -3.5 40.6, -3.5 40.17))"
sql = ("SELECT * FROM natural where type='park' and name is not null limit {}"
       .format(limit))
data_source = ogr.Open(data_path)
layer = data_source.ExecuteSQL(
    sql,
    # ogr.CreateGeometryFromWkt(wkt_spatial_filter)
    )
print(len(layer))
svg_tag = madrid_parks(layer, destination_path, item_scale, group_scale)
spatial_filter_svg = affinity.scale(from_wkt(wkt_spatial_filter), group_scale, group_scale)
# svg_tag.set_polygon(spatial_filter_svg.svg())

file = open(destination_path, 'w')
file.write(svg_tag.render())
