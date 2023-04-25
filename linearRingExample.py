from shapely import LinearRing
from linearRingSVG import linearRingSVG
from writeSVG import writeSVG

lr = LinearRing([(0, 0), (200, 0), (200, 200), (0, 200)])
lr2 = LinearRing([(50, 50), (250, 50), (250, 200), (50, 250)])
b = lr.buffer(3)
contentStr = linearRingSVG(lr2,  'red', 3) + \
    linearRingSVG(lr,  'blue', 3)
writeSVG('linear-ring-example.svg', contentStr)
