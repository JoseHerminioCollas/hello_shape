from shapely import polygons
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from write_svg import write_svg
from get_svg_element import get_svg_element

def shape_data_to_svg(shape_data):
 feature=shape_data[0][3]
 feature_coords=get_feature_coords(feature)
 shapely_polygon=polygons(feature_coords)
 d_path_value=get_svg_d_path(shapely_polygon)
 content=get_svg_element(d_path_value)
 write_svg(content)
 return True