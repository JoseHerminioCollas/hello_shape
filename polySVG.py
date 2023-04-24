def polySVG(polygon, color, strokeWeight='1'):
 # make string for polygon from polygon coordinates
 strA = ''
 for x, y in polygon.coords:
  strA += str(x) + ',' + str(y) + ' '
  # print(x, y)
 # print(strA)
 return ' <polygon points="{0}" fill="{1}" stroke="{1}" stroke-width="{2}" />'.format(strA, color, strokeWeight)