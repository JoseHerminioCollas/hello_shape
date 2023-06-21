import math

def writeData(fileName, steps):
    f = open(fileName, 'w')
    currAngle = 0
    angleIncrement = math.pi * 0.1
    spiralRadius = 3
    spiralRadiusIncrement = 0.2
    circleRadius = 0.5
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

    f.write(data.__str__())
    return data
