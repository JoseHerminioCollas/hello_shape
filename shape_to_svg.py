from osgeo import ogr
from shapely import polygons
from get_feature_coords import get_feature_coords
from get_svg_d_path import get_svg_d_path
from write_svg import write_svg

dataPath="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
data=ogr.Open(dataPath)

feature=data[0][3]
featureCoords=get_feature_coords(feature)
shapelyPolygon=polygons(featureCoords)
pathValue=get_svg_d_path(shapelyPolygon)

def shape_to_svg():
 write_svg(pathValue)
 return True