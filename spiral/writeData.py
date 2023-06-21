import math

def writeData(fileName,
              steps,
              circleRadiusStart, circleRadiusIncrement,
              spiralRadiusStart, spiralRadiusIncrement,
              angleIncrement):
    currAngle = 2
    spiralRadius = spiralRadiusStart
    circleRadius = circleRadiusStart
    data = []
    i = 0
    while i <= steps:
        x = math.cos(currAngle) * spiralRadius
        y = math.sin(currAngle) * spiralRadius
        currAngle = currAngle + angleIncrement
        spiralRadius = spiralRadius + spiralRadiusIncrement
        d = {'circleRadius': circleRadius, 'x': x, 'y': y}
        data.append(d)
        circleRadius += circleRadiusIncrement
        i += 1

    f = open(fileName, 'w')
    f.write(data.__str__())
    return data
