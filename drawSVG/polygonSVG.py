
def polygonSVG(polygon, color='red'):
 po = polygon.exterior.coords
 strA = ''
 for x, y in po:
  strA += str(x) + ',' + str(y) + ' '

 return ' <polygon points="{0}" fill="{1}" stroke="none" />'.format(strA, color)
