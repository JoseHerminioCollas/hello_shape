from osgeo import ogr
from shape_data_to_svg import shape_data_to_svg

def test_shape_data_to_svg():
 data_path="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
 shape_data=ogr.Open(data_path)
 assert shape_data_to_svg(shape_data)==True