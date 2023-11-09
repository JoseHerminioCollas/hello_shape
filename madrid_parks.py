import os
from osgeo import ogr
from Features import Features
from SVGTag import SVGTag
limit=200
config =     {
        'path':
            'data/Madrid-shp/shape/natural.shp',
        'sql':
            "SELECT * FROM natural where type='park' and name is not null limit {}"
            .format(3),
        'destination': os.environ.get('FILE_DESTINATION'),
    }
def madrid_parks(
        data_path=config['path'],
          sql=config['sql'],
          destination_path=config['destination']
          ):
    data_source = ogr.Open(data_path)
    layer = data_source.ExecuteSQL(sql)
    features = Features(layer, 3, 1000)
    svg_tag = SVGTag()
    for i in range(0, len(features.data)):
        svg_tag.set_polygon(features.scaled_group.geoms[i].svg())
        svg_tag.set_text_element(
            features.data[i]['properties']['name'],
            features.scaled_group.geoms[i].centroid.x, features.scaled_group.geoms[i].centroid.y,
            3
        )
    j = open(destination_path, 'w')
    j.write(svg_tag.render())
madrid_parks(config['path'])