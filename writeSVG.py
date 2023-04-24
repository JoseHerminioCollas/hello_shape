def writeSVG(fileName, content):
 fileName = 'line-difference.svg'
 f = open(fileName, 'w')
 # write the contents of the SVG file
 f.write('<svg width="400" height="400" fill="black" stroke="black">')
 f.write(content)
 f.write('</svg>')
 return 'x'