from shapely import Polygon, LinearRing
from drawSVG.polygonSVG import polygonSVG
from drawSVG.linearRingSVG import linearRingSVG
from writeSVG.writeSVG import writeSVG

coords = ((50, 0), (0, 100), (100, 100), (100, 0.), (0., 0.))
polygon = Polygon(coords)
svg = polygonSVG(polygon)

coords = ((50, 50), (110, 150), (150, 150), (150, 50.), (50., 50.))
polygon = Polygon(coords)
svgB = polygonSVG(polygon, 'peru')

bp = polygon.buffer(13)
bp = polygonSVG(bp, 'gray')

contentStr = ''
contentStr += bp
# contentStr += svg
contentStr += svgB

writeSVG('../generated/polygon-example.svg', contentStr)
