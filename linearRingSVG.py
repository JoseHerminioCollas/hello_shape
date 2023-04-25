def linearRingSVG(linearRing, color='red', strokeWeight='1'):
 strA = ''
 for x, y in linearRing.coords:
  strA += str(x) + ',' + str(y) + ' '
 return ' <polygon points="{0}" fill="{1}" stroke="{1}" stroke-width="{2}" />'.format(strA, color, strokeWeight)
