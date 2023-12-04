from SVGTag import SVGTag
from shapely import MultiPolygon, Polygon, affinity, box, Point, from_geojson, is_valid, to_wkt
from osgeo import ogr
from point_buff_to_box import point_buff_to_box


def natural(
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
    extent_box = Polygon.from_bounds(extent[0], extent[1], extent[2], extent[3])
    user_spat_filter = point_buff_to_box(cx, cy, buffer)
    # if the users' selected area is not in the extent the return False
    if not user_spat_filter.overlaps(extent_box):
        return False
    if view_spat_area:
        polys.append(user_spat_filter)
    # make the geospatial filter if requested
    geospatial_filter = None
    if use_spat:
        geospatial_filter = ogr.CreateGeometryFromWkt(to_wkt(user_spat_filter))
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
        fgj = affinity.scale(from_geojson(geo_json), item_scale, item_scale)
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
