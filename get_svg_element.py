def get_svg_element(d):
 content='<svg viewBox="-100 -100 100 100" width="200" height="200">'
 content+='<rect width="20" height="200" x="-20" y="-20" fill="blue" />'
 content+='<g transform-origin="center" transform="scale(1)">'
 content+='<path d="{0}" fill="red" stroke="green" />'.format(d)
 content+='</g></svg>'
 
 return content