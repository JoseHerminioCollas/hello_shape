import math
from writeData import writeData
from writeSVG import writeSVG
data = writeData('data-1',
                 350,
                 0.5, .01,
                 2, 0.095,
                 math.pi * 0.15)
writeSVG('spiral-1.svg', data)
