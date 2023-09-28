from osgeo import ogr
import json
data = ogr.Open("/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp")
print('Data Name:', data.GetName())
for layer in data:
    print(':::', layer.GetName())
    # layer_defn = layer.GetLayerDefn()
    # for i in range(layer_defn.GetFieldCount()):
        # print(layer_defn.GetFieldDefn(i).GetName())
    # for i in range(layer_defn.GetGeomFieldCount()):
        # print(layer_defn.GetGeomFieldDefn(i).GetName(), layer_defn.GetGeomFieldDefn(i).GetType())
    # layer.ResetReading()
    for i in range(0,10):
        f=layer[i]
        id=f.GetFID()
        j=f.ExportToJson()
        k=json.loads(j)
        readable=f.DumpReadable()
        print(id)
        print(k['type'])
        # print(readable)
        print('---', f.geometry().GetGeometryType()) 