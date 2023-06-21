import math
from writeData import writeData
from writeSVG import writeSVG

data = writeData('data-1', 350, 0.5, math.pi * 0.1)
writeSVG('spiral-1.svg', data)
