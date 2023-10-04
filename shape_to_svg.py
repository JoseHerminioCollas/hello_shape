import re

def shape_to_svg(shapely_object, color):
    path_tag=re.sub(r'stroke="#\d+" ', '', shapely_object.svg(0.25, color, 1.0))
    return path_tag