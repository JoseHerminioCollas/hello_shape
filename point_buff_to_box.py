from shapely import Point, box


def point_buff_to_box(cx, cy, buffer):
    p = Point(cx, cy)
    point_buff = p.buffer(buffer)
    point_bounds = point_buff.bounds
    geo_spat_box = box(point_bounds[0], point_bounds[1], point_bounds[2], point_bounds[3])
    return geo_spat_box
