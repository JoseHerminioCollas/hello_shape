# from shapely.geometry import Polygon
import geopandas as gpd
import matplotlib.pyplot as plt

from shapely import GeometryCollection, LinearRing, LineString, MultiLineString, MultiPoint, Point, Polygon, buffer
# from shapely import LineString, Point, Polygon, BufferCapStyle, BufferJoinStyle

buffer(Point(10, 10), 2, quad_segs=1)
# <POLYGON ((12 10, 10 8, 8 10, 10 12, 12 10))>

buffer(Point(10, 10), 2, quad_segs=2)
# <POLYGON ((12 10, 11.414 8.586, 10 8, 8.586 8.586, 8 10, 8.5...>

buffer(Point(10, 10), -2, quad_segs=1)
# <POLYGON EMPTY>

line = LineString([(10, 10), (20, 10)])

buffer(line, 2, cap_style="square")
# <POLYGON ((20 12, 22 12, 22 8, 10 8, 8 8, 8 12, 20 12))>

buffer(line, 2, cap_style="flat")
# <POLYGON ((20 12, 20 8, 10 8, 10 12, 20 12))>

buffer(line, 2, single_sided=True, cap_style="flat")
# <POLYGON ((20 10, 10 10, 10 12, 20 12, 20 10))>

line2 = LineString([(10, 10), (20, 10), (20, 20)])

l3 = buffer(line2, 2, cap_style="flat", join_style="bevel")
# <POLYGON ((18 12, 18 20, 22 20, 22 10, 20 8, 10 8, 10 12, 18 12))>

buffer(line2, 2, cap_style="flat", join_style="mitre")
# <POLYGON ((18 12, 18 20, 22 20, 22 8, 10 8, 10 12, 18 12))>

buffer(line2, 2, cap_style="flat", join_style="mitre", mitre_limit=1)
# <POLYGON ((18 12, 18 20, 22 20, 22 9.172, 20.828 8, 10 8, 10 12, 18 12))>

square = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])

buffer(square, 2, join_style="mitre")
# <POLYGON ((-2 -2, -2 12, 12 12, 12 -2, -2 -2))>

buffer(square, -2, join_style="mitre")
# <POLYGON ((2 2, 2 8, 8 8, 8 2, 2 2))>

buffer(square, -5, join_style="mitre")
# <POLYGON EMPTY>

buffer(line, float("nan")) is None
# True

# a = Polygon([[0, 0], [11, 0], [1, 1], [0, 1], [0, 0]])
poly1 = Polygon( [(1, 0), (1,0), (1,1), (0,1) ] )
poly2 = Polygon( [(0.25, 0.25), (0.5,0.25), (0.5,0.5), (0.25,0.5) ] )
polydiff = poly1.difference(poly2)
#axis("off")
# myPoly = gpd.GeoSeries([l3 ])
p = Point(100, 100)
p2 = Point(10, 1)
m2 = gpd.GeoSeries([p, p2])
# myPoly.to_file('x', driver="png")
# plot before save with ply
m2.plot()
plt.show()
plt.savefig("generated-graph.svg")
