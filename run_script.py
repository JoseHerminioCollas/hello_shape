from madrid_parks import madrid_parks
import sys
from osgeo import ogr

data_path = 'data/Madrid-shp/shape/natural.shp'
destination_path = '__generated/madrid_parks_11_9.svg'
sql = "SELECT * FROM natural where type='park' and name is not null limit {}".format(300)
data_source = ogr.Open(data_path)
layer = data_source.ExecuteSQL(sql)
print(len(layer))
madrid_parks(layer, destination_path)
