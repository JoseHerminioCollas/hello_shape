from Features import Features
from SVGTag import SVGTag
from shapely import to_wkt, affinity, box
from osgeo import ogr

def madrid_natural(item_scale,group_scale,data_path,styles):
    spat_box = box(-3.76, 40.36, -3.72, 40.4)
    spat_box_scaled = affinity.scale(spat_box, group_scale, group_scale)
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
        .format(10000))
    sql_water = ("SELECT * FROM natural where type='water' and name is not null limit {}"
        .format(3000))

    data_source = ogr.Open(data_path)

    park_layer = data_source.ExecuteSQL(
        sql_park,
        ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )
    water_layer = data_source.ExecuteSQL(
        sql_water,
        ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )

    features_park = Features(park_layer, item_scale, group_scale)
    svg_park = '<g class="{}">'.format('parks')
    for i in range(0, len(features_park.data)):
        svg_park += features_park.scaled_group.geoms[i].svg()
    svg_park += '</g>'

    features_park = Features(water_layer, item_scale, group_scale)
    svg_water = '<g class="{}">'.format('water')
    for i in range(0, len(features_park.data)):
        svg_water += features_park.scaled_group.geoms[i].svg()
        svg_water += ('<text x="{}" y="{}">{}</text>'
        .format(
            features_park.scaled_group.geoms[i].centroid.x,
            features_park.scaled_group.geoms[i].centroid.y,
            features_park.data[i]['properties']['name']
        ))
    svg_water += '</g>'
    # build the SVGTag
    svg_tag = SVGTag(styles)
    svg_tag.prepend(
        spat_box_scaled.svg()
    )
    svg_tag.append(svg_park)
    svg_tag.append(svg_water)

    return svg_tag.render()
