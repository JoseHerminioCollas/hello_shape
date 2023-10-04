from shape_to_svg import shape_to_svg
from shapely import from_geojson

def feature_to_svg(feature):
 geojson = feature.ExportToJson()
 shape_one=from_geojson(geojson)
 shape_feature_svg=shape_to_svg(shape_one, 'red')
 return shape_feature_svg