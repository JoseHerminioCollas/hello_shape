import madrid_parks from madrid_parks
import sys
from osgeo import ogr
limit=200
config =     {
        'path':
            'data/Madrid-shp/shape/natural.shp',
        'sql':
            "SELECT * FROM natural where type='park' and name is not null limit {}"
            .format(3),
        'destination': os.environ.get('FILE_DESTINATION'),
    }

# layer destination_path
   data_source = ogr.Open(data_path)
    layer = data_source.ExecuteSQL(sql)
 
madrid_parks(sys.argv[0], sys.argv[1], sys.argv2)