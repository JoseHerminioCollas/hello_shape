from SVGTag import SVGTag
from layer_to_svg import layer_to_svg
from shapely import to_wkt, affinity, box
from osgeo import ogr

item_scale = 3
group_scale = 1500
limit = 1000
data_path = 'data/Madrid-shp/shape/natural.shp'
destination_path = '__generated/madrid_parks_11_14.svg'
spat_box = box(-3.5, 40.17, -3.2, 40.6)
spat_box_scaled = affinity.scale(spat_box, group_scale, group_scale)
sql = ("SELECT * FROM natural where type='park' and name is not null limit {}"
       .format(limit))
data_source = ogr.Open(data_path)
print('data_source created: ', data_source)

layer = data_source.ExecuteSQL(
    sql,
    ogr.CreateGeometryFromWkt(to_wkt(spat_box))
)
print(len('layer created: '), layer)

file = open('style.css', 'r', encoding='utf-8')
svg_tag = SVGTag(file.read())
svg_tag.prepend(
    spat_box_scaled.svg()
)
svg_tag.append(
    layer_to_svg(layer, 'parks', item_scale, group_scale)
)
print('SVG tag created: ', svg_tag)

file = open(destination_path, 'w')
file.write(svg_tag.render())
print('File created: ', file)