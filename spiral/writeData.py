import math

def writeData(fileName, steps, circleRadiusStart, spiralRadiusIncrement, angleIncrement):
    currAngle = 2
    spiralRadius = 2
    circleRadius = circleRadiusStart
    data = []
    i = 0
    while i <= steps:
        currAngle = currAngle + angleIncrement
        x = math.cos(currAngle) * spiralRadius
        y = math.sin(currAngle) * spiralRadius
        spiralRadius = spiralRadius + spiralRadiusIncrement
        d = {'circleRadius': circleRadius, 'x': x, 'y': y}
        data.append(d)
        circleRadius += .01
        i += 1

    f = open(fileName, 'w')
    f.write(data.__str__())
    return data
