from osgeo import ogr
import json

dataPath="/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
data=ogr.Open(dataPath)
# layer feature
a=data[0][0].ExportToJson()
b=json.loads(a)
c=b['geometry']['coordinates']
print(c[0][0][0])
print(b['geometry']['type'])
