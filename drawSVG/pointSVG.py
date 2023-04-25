def pointSVG(point, color='blue', radius=1):
 cx = point.x
 cy = point.y
 z = '<circle r="{3}" cx="{0}" cy="{1}" fill="{2}" stroke="none" />'.format(cx, cy, color, radius)
 return z
