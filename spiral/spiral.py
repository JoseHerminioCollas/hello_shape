import math
from writeData import writeData
from writeSVG import writeSVG
# data = writeData('data-1',
#                  350,
#                  0.5, .01,
#                  2, 0.095,
#                  math.pi * 0.15)
# writeSVG('spiral-1.svg', data)

i = 1
circleRadiusIncrement = .01
angleIncrement = math.pi * 0.15
while i <= 10:
    data = writeData('data-{0}'.format(i),
                     350,
                     0.5, circleRadiusIncrement,
                     2, 0.095,
                     angleIncrement)
    writeSVG('spiral-{0}.svg'.format(i), data)
    circleRadiusIncrement += 0.0005
    angleIncrement += .01
    print('data-{0}'.format(i))
    i += 1
