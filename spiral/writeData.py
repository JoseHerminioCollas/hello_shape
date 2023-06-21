import math

def writeData(fileName, steps, circleRadius,angleIncrement):
    currAngle = 2
    spiralRadius = 2
    spiralRadiusIncrement = 0.1
    data = []
    i = 0
    while i <= steps:
        currAngle = currAngle + angleIncrement
        x = math.cos(currAngle) * spiralRadius
        y = math.sin(currAngle) * spiralRadius
        spiralRadius = spiralRadius + spiralRadiusIncrement
        d = {'circleRadius': circleRadius, 'x': x, 'y': y}
        data.append(d)
        i += 1

    f = open(fileName, 'w')
    f.write(data.__str__())
    return data
