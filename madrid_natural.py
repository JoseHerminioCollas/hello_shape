from SVGTag import SVGTag
from layer_to_svg import layer_to_svg
from shapely import to_wkt, affinity, box
from osgeo import ogr

def madrid_natural(item_scale,group_scale,data_path,styles):
    spat_box = box(-3.76, 40.36, -3.72, 40.4)
    spat_box_scaled = affinity.scale(spat_box, group_scale, group_scale)
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
        .format(10000))
    sql_water = ("SELECT * FROM natural where type='water' and name is not null limit {}"
        .format(3000))

    data_source = ogr.Open(data_path)

    layer = data_source.ExecuteSQL(
        sql_park,
        ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )
    layer2 = data_source.ExecuteSQL(
        sql_water,
        ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )

    svg_tag = SVGTag(styles)
    svg_tag.prepend(
        spat_box_scaled.svg()
    )
    svg_tag.append(
        layer_to_svg(layer, 'parks', 1, group_scale)
    )
    svg_tag.append(
        layer_to_svg(layer2, 'water', item_scale, group_scale)
    )

    return svg_tag.render()
