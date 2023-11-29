from Features import Features
from SVGTag import SVGTag
from shapely import MultiPolygon, affinity, box, Point, from_geojson, is_valid, to_wkt
from osgeo import ogr


def natural_2(
        item_scale,
        group_scale,
        data_path,
        styles,
        cx=None,
        cy=None,
        buffer=0.2,
        use_spat=True,
        view_spat_area=True,
):
    polys = []
    data_source = ogr.Open(data_path)
    layer = data_source.GetLayer()
    extent = layer.GetExtent()
    # TODO if center not in extent throw error
    # make a Shapely box of the SPAT filter inputs: cx, cy, buffer
    p = Point(cx, cy)
    point_buff = p.buffer(buffer)
    point_bounds = point_buff.bounds
    geo_spat_box = box(point_bounds[0], point_bounds[1], point_bounds[2], point_bounds[3])
    if view_spat_area:
        polys.append(geo_spat_box)
    # make the geospatial filter if requested
    geospatial_filter = None
    if use_spat:
        geospatial_filter = ogr.CreateGeometryFromWkt(to_wkt(geo_spat_box))
    # get the layer
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
                .format(50000))
    park_layer = data_source.ExecuteSQL(
        sql_park,
        geospatial_filter
    )
    # populate polygons
    for f in park_layer:
        geo_json = f.ExportToJson()
        fgj = from_geojson(geo_json)
        if is_valid(fgj):
            polys.append(fgj)
    mp = MultiPolygon(polys)
    scaled_poly = affinity.scale(
        mp,
        group_scale, -group_scale
    )
    # set the SVGTag object
    svg_tag = SVGTag(styles)
    svg_tag.append(scaled_poly.svg(), 'a')
    return svg_tag.render()
