import math

# generate spiral
steps = 350
currAngle = 0
angleIncrement = math.pi * 0.1
spiralRadius = 3
spiralRadiusIncrement = 0.2
circleRadius = 0.5
offSet = 100

# write a spiral
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

# print("a", data)
# write spiral
    # rowS += tagString.format(circleRadius, y, x)

fileName = 'spiral-1.svg'
f = open(fileName, 'w')

rowS = ''
tagString = '<circle r="{0}" cx="{2}" cy="{1}" fill="none" stroke="black" stroke-width="0.1mm" />'
# write the contents of the SVG file 0.01mm
f.write('<svg width="200" height="200" fill="none" stroke="black">')
f.write('<circle r="30" cx="100" cy="100" stroke-width="0.1mm" />')
for e in data:
    print(e['x'])
    s = tagString.format(e['circleRadius'], e['y'], e['x'])
    f.write(s)
f.write('<text x="25" y="58.9" font-size="2.25" fill="black" stroke-width="0.01mm">VERICITE</text>')
f.write('</svg>')
