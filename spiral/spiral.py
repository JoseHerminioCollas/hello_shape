from writeData import writeData
from writeSVG import writeSVG

data = writeData('data', 350)
writeSVG('spiral-2.svg', data)