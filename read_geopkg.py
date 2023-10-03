from osgeo import ogr

data_path="/home/goat/projects/hello_shape/data/xxx.gpkg"
shape_data=ogr.Open(data_path)
for d in shape_data:
 for f in d:
  name=f.GetField('NAME')
  print(name)