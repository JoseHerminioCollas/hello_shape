import re

def get_svg_d_path(shapelyPolygon):
 pSVG=shapelyPolygon.svg()
 regexpA=re.compile(r'd="(.*)"')
 m=regexpA.search(pSVG)
 return m.groups()[0]