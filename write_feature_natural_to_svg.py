import json
from osgeo import ogr, osr
from shapely import  affinity,from_geojson, MultiPolygon, transform,ops
from get_svg_document import get_svg_document
from get_geo_data import get_geo_data
from get_text_svg_element import get_text_svg_element

data_path='/home/goat/projects/hello_shape/data/map.osm'
# data_path='/home/goat/projects/hello_shape/data/geography_regions_elevation/ne_50m_geography_regions_elevation_points.shp'
# data_path='/home/goat/projects/hello_shape/data/Madrid-shp/shape/natural.dbf'
# osr.SpatialReference().SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
# driver = ogr.GetDriverByName("ESRI Shapefile")
# source = driver.Open(data_path,0)
data_source=ogr.Open(data_path)
for l in data_source:
 for f in l:
  z=f.ExportToJson()
  s=from_geojson(z)
  x=ops.transform(lambda x, y: (y, x), s)
  print(x)
exit()
layers=source[0]
# OGR features to geo json Python data
geo_data=get_geo_data(layers,len(layers))
shape_num=20
# import osgeo

# srs = SpatialReference()
# # GDAL 3 changes axis order: https://github.com/OSGeo/gdal/issues/1546
# srs.SetAxisMappingStrategy(osgeo.osr.OAMS_TRADITIONAL_GIS_ORDER)

def scale_shape(k):
 el=from_geojson(json.dumps(geo_data[k]))
 el2=affinity.scale(el,1,1)
 return el2

polygons=[scale_shape(k) for k in range(shape_num)]
# x=transform(polygons, lambda x,: [y,x] )
print(polygons)
exit

mp=MultiPolygon(polygons)
mp2=affinity.scale(mp,2000,2000)

doc=''
doc+=mp2.svg(1,'red',1.0)
# write text
for i in range(0,shape_num):
 el2=mp2.geoms[i]
 doc+=get_text_svg_element(
  el2.centroid.x,
  el2.centroid.y,
  geo_data[i]['properties']['name'],
  4
  )

f=open('generated/features_10_13_c_2023.svg', 'w')
f.write(get_svg_document(doc))