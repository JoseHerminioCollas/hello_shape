from SVGTag import SVGTag
from madrid_parks import madrid_parks
from shapely import from_wkt, to_wkt, affinity, box
from osgeo import ogr

item_scale = 3
group_scale = 1500
limit = 1000
data_path = 'data/Madrid-shp/shape/natural.shp'
destination_path = '__generated/madrid_parks_11_10.svg'
spat_box = box(-3.5, 40.17, -3.2, 40.6)
spat_box_scaled = affinity.scale(spat_box, group_scale, group_scale)
print(spat_box)
wkt_spatial_filter = "POLYGON ((-3.5 40.17, -3.2 40.17, -3.2 40.6, -3.5 40.6, -3.5 40.17))"
sql = ("SELECT * FROM natural where type='park' and name is not null limit {}"
       .format(limit))
data_source = ogr.Open(data_path)
layer = data_source.ExecuteSQL(
    sql,
    ogr.CreateGeometryFromWkt(to_wkt(spat_box))
)
print(len(layer))
svg_tag = SVGTag()
svg_tag.set_polygon(spat_box_scaled.svg())
madrid_parks(svg_tag, layer, item_scale, group_scale)

file = open(destination_path, 'w')
file.write(svg_tag.render())
