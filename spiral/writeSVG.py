def writeSVG(fileName, data):
    f = open(fileName, 'w')
    tagString = '<circle r="{0}" cx="{2}" cy="{1}" fill="none" stroke="black" stroke-width="0.1mm" />'
    f.write('<svg width="200" height="200" fill="none" stroke="black">')
    f.write('<circle r="30" cx="100" cy="100" stroke-width="0.1mm" />')
    for e in data:
        circleSVG = tagString.format(e['circleRadius'], e['y'], e['x'])
        f.write(circleSVG)
    f.write('<text x="25" y="58.9" font-size="2.25" fill="black" stroke-width="0.01mm">VERICITE</text>')
    f.write('</svg>')
