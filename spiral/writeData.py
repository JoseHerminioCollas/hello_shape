import math

def writeData(fileName, steps, circleRadius,angleIncrement):
    currAngle = 0
    spiralRadius = 3
    spiralRadiusIncrement = 0.2
    offSet = 100
    data = []
    i = 0
    while i <= steps:
        currAngle = currAngle + angleIncrement
        x = math.cos(currAngle) * spiralRadius + offSet
        y = math.sin(currAngle) * spiralRadius + offSet
        spiralRadius = spiralRadius + spiralRadiusIncrement
        d = {'circleRadius': circleRadius, 'x': x, 'y': y}
        data.append(d)
        i += 1

    f = open(fileName, 'w')
    f.write(data.__str__())
    return data
