from get_svg_text_element import get_svg_text_element

def get_svg(poly, data):
 svg=poly.svg()
 svg+=get_svg_text_element(
  data['properties']['name'],
  poly.centroid.x,
  poly.centroid.y,
 )
 return svg
