from Features import Features
from SVGTag import SVGTag
from shapely import MultiPolygon, affinity, box, Point, from_geojson, is_valid, to_wkt
from osgeo import ogr


def natural_2(
        item_scale,
        group_scale,
        data_path,
        styles,
        spatial_filter=None,
        center=None
):
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
                .format(50000))
    data_source = ogr.Open(data_path)
    layer = data_source.GetLayer()
    extent = layer.GetExtent()
    # extent = (-4.0699641, -3.2300143, 40.170042, 40.6499669)
    exmidx = extent[0] - ((extent[0] - extent[1]) / 2)
    exmidy = extent[2] - ((extent[2] - extent[3]) / 2)
    # extent_center = Point(x, y)
    # print('extent', extent, exmidx)
    # point to geometry for SQL statement
    p = Point(exmidx + 0.05, exmidy + 0.04)
    point_buff = p.buffer(0.2)
    point_bounds = point_buff.bounds
    sbox = box(point_bounds[0], point_bounds[1], point_bounds[2], point_bounds[3])
    park_layer = data_source.ExecuteSQL(
        sql_park,
        ogr.CreateGeometryFromWkt(to_wkt(sbox))
    )
    scale = 1000
    polys = []
    for f in park_layer:
        geo_json = f.ExportToJson()
        fgj = from_geojson(geo_json)
        if is_valid(fgj):
            polys.append(fgj)
    # set up the style here
    polys.append(sbox)
    mp = MultiPolygon(polys)
    scaled_poly = affinity.scale(
        mp,
        scale, -scale
    )
    svg_tag = SVGTag(styles)
    # svg_tag.append(sbox.svg(), 'target_area')
    svg_tag.append(scaled_poly.svg(), 'a')
    return svg_tag.render()
