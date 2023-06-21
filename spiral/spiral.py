import math
from writeData import writeData
from writeSVG import writeSVG
# Increase the circle size incrementally 0.003
circleRadiusIncrement = 0.002
# The spiral is drawn by dot
angleIncrement = math.pi * 0.13
i = 1
while i <= 10:
    data = writeData('data-{0}'.format(i),
                     350,
                     0.2, circleRadiusIncrement,
                     2, 0.095,
                     angleIncrement)
    writeSVG('spiral-{0}.svg'.format(i), data)
    # circleRadiusIncrement += 0.0005
    angleIncrement += 0.1
    print('data-{0}'.format(i))
    i += 1
