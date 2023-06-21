import math
from writeData import writeData
from writeSVG import writeSVG
# 'data-1', 350, 0.5, math.pi * 0.15
# 'data-1', 350, 0.5, 0.1, math.pi * 0.15
data = writeData('data-1', 350, 0.5, 0.1, math.pi * 0.15)
writeSVG('spiral-1.svg', data)
