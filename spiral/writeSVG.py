def writeSVG(fileName, data):
    f = open(fileName, 'w')
    tagString = '<circle r="{0}" cx="{2}" cy="{1}" fill="none" stroke="black" stroke-width="0.1" />'
    f.write('<svg width="380" height="380" fill="none" stroke="black" viewBox="0 0 380 380" transform="scale(4)">')
    f.write('<circle r="40" cx="40" cy="40" stroke-width="0.1" />')
    for e in data:
        offset = 40
        x = e['x'] + offset
        y = e['y'] + offset
        circleSVG = tagString.format(e['circleRadius'], y, x)
        f.write(circleSVG)
    f.write('<text x="36" y="78" font-size="2" font-family="Arial, Helvetica, sans-serif" fill="black" stroke="none">VARICITE</text>')
    f.write('</svg>')
