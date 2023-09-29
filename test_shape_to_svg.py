from shape_to_svg import shape_to_svg

def test_shape_to_svg():
 dataPath="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
 assert shape_to_svg(dataPath)==True