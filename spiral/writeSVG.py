def writeSVG(fileName, data):
    f = open(fileName, 'w')
    tagString = '<circle r="{0}" cx="{2}mm" cy="{1}mm" fill="none" stroke="black" stroke-width="0.1mm" />'
    f.write('<svg width="80mm" height="80mm" fill="none" stroke="black">')
    f.write('<circle r="40mm" cx="40mm" cy="40mm" stroke-width="0.1mm" />')
    for e in data:
        offset = 40
        x = e['x'] + offset
        y = e['y'] + offset
        circleSVG = tagString.format(e['circleRadius'], y, x)
        f.write(circleSVG)
    f.write('<text x="72mm" y="145mm" font-size="6" fill="black" stroke-width="0.01mm">VERICITE</text>')
    f.write('</svg>')
