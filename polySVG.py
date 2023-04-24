def polySVG(polygon, color):
 # make string for polygon from polygon coordinates
 strA = ''
 for x, y in polygon.exterior.coords:
  strA += str(x) + ',' + str(y) + ' '
  # print(x, y)
 print(strA)
 return ' <polygon points="{0}" fill="{1}" />'.format(strA, color)