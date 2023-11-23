from Features import Features
from SVGTag import SVGTag
from shapely import to_wkt, affinity, box
from osgeo import ogr

def natural(item_scale,group_scale,data_path,styles,spat_zoom=0,center=None):
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
        .format(90000))
    sql_water = ("SELECT * FROM natural where type='water' and name is not null limit {}"
        .format(3000))
    # get the data source
    data_source = ogr.Open(data_path)
    # a=data_source.GetLayerCount()
    b=data_source.GetLayer()
    c=b.GetExtent()
    # print('a', b, c)
    spat_box2 = box(c[0], c[2], c[1], c[3])
    spat_box2_scaled=affinity.scale(spat_box2, group_scale,group_scale)
    spat_box3=affinity.scale(spat_box2_scaled, -0.5,-0.5)
    spat_box4=affinity.scale(spat_box3, -0.5,-0.5)
    # get the one or more layers
    park_layer = data_source.ExecuteSQL(
        sql_park,
        # ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )
    spat_box = box(-3.76, 40.36, -3.72, 40.4)
    spat_box_scaled = affinity.scale(spat_box, group_scale, group_scale)
    water_layer = data_source.ExecuteSQL(
        sql_water,
        # ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )
    f=water_layer.GetExtent()
    # build out the one or more features
    features_park = Features(park_layer, item_scale, group_scale)
    features_water = Features(water_layer, item_scale, group_scale)
    # build the one SVGTag and return its output
    svg_tag = SVGTag(styles)
    svg_tag.prepend(spat_box2_scaled.svg())
    svg_tag.append(spat_box3.svg(), 'extent-level-1')
    svg_tag.append(spat_box4.svg(), 'extent-level-2')
    svg_tag.append_shapes(features_water.scaled_group.geoms, features_water.data, 'water', False)
    svg_tag.append_shapes(features_park.scaled_group.geoms, features_park.data, 'parks', False)
    return svg_tag.render()
