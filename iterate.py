from osgeo import ogr
# daShapefile = r"/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp"
data = ogr.Open("/home/goat/projects/hello_shape/data/countries/ne_10m_admin_0_countries.shp")

print('Data Name:', data.GetName())

# get a layer with GetLayer('layername'/layerindex)
for layer in data:
    print('Layer Name:', layer.GetName())
    print('Layer Feature Count:', len(layer))
    # each layer has a schema telling us what fields and geometric fields the features contain
    print('Layer Schema')
    layer_defn = layer.GetLayerDefn()
    for i in range(layer_defn.GetFieldCount()):
        print(layer_defn.GetFieldDefn(i).GetName())
    # some layers have multiple geometric feature types
    # most of the time, it should only have one though
    for i in range(layer_defn.GetGeomFieldCount()):
        # some times the name doesn't appear
        # but the type codes are well defined
        print(layer_defn.GetGeomFieldDefn(i).GetName(), layer_defn.GetGeomFieldDefn(i).GetType())
    # get a feature with GetFeature(featureindex)
    # this is the one where featureindex may not start at 0
    layer.ResetReading()
    for feature in layer:
        # print('Feature ID:---', feature.GetFID())
        # # get a metadata field with GetField('fieldname'/fieldindex)
        # print('Feature Metadata Keys:', feature.keys())
        # print('Feature Metadata Dict:', feature.items())
        print('Feature Geometry:---', feature.geometry())  