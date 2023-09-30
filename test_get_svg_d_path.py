from get_svg_d_path import get_svg_d_path

class PolygonMock:
 def svg(self):
  return 'd="x"'
polygon_mock=PolygonMock()
def test_get_svg_d_path():
 assert isinstance(get_svg_d_path(polygon_mock),str)