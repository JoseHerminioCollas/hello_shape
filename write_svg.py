def write_svg(d):
 content='<path d="{0}" fill="red" stroke="green" />'.format(d)
 openTag='<svg viewBox="-100 -100 100 100" width="200" height="200">'
 bGTag='<rect width="20" height="200" x="-20" y="-20" fill="blue" />'
 openG='<g transform-origin="center" transform="scale(1)">'
 f=open('countries.svg', 'w')
 f.write(openTag)
 f.write(bGTag)
 f.write(openG)
 f.write(content)
 f.write('</g></svg>')