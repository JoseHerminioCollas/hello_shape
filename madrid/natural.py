from Features import Features
from SVGTag import SVGTag
from shapely import to_wkt, affinity, box
from osgeo import ogr

def natural(item_scale,group_scale,data_path,styles):
    spat_box = box(-3.76, 40.36, -3.72, 40.4)
    spat_box_scaled = affinity.scale(spat_box, group_scale, group_scale)
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
        .format(10000))
    sql_water = ("SELECT * FROM natural where type='water' and name is not null limit {}"
        .format(3000))
    # get the data source
    data_source = ogr.Open(data_path)
    # get the one or more layers
    park_layer = data_source.ExecuteSQL(
        sql_park,
        ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )
    water_layer = data_source.ExecuteSQL(
        sql_water,
        ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )
    # build out the one or more features
    features_park = Features(park_layer, item_scale, group_scale)
    features_water = Features(water_layer, item_scale, group_scale)
    # build the one SVGTag and return its output
    svg_tag = SVGTag(styles)
    svg_tag.append_shapes(features_water.scaled_group.geoms, features_water.data, 'water', True)
    svg_tag.append_shapes(features_park.scaled_group.geoms, features_park.data, 'parks', True)
    svg_tag.prepend(spat_box_scaled.svg())

    return svg_tag.render()
