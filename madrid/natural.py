from Features import Features
from SVGTag import SVGTag
from shapely import MultiPolygon, affinity, box, Point, from_geojson,is_valid
from osgeo import ogr

def natural(item_scale,group_scale,data_path,styles,spat_zoom=0,center=None):
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
        .format(500))
    sql_water = ("SELECT * FROM natural where type='water' and name is not null limit {}"
        .format(3000))
    data_source = ogr.Open(data_path)
    # a=data_source.GetLayerCount()
    b=data_source.GetLayer()
    extent=b.GetExtent()
    print('extent', extent)
    # extent (-4.0699641, -3.2300143, 40.170042, 40.6499669)
    p=Point(-4.0,40.7)
    point_buff=p.buffer(0.1)
    point_bounds=point_buff.bounds
    # a POINT (-4.01 40.16) (-104.01, -59.84, 95.99, 140.16)
    # box_a=box(point_bounds[0],point_bounds[2],point_bounds[1],point_bounds[3])
    # box_b=box(point_bounds[0],point_bounds[1],point_bounds[2],point_bounds[3])
    spat_box2 = box(extent[0], extent[2], extent[1], extent[3])
    spat_box2_scaled=affinity.scale(spat_box2, group_scale,group_scale)
    # spat_box3=affinity.scale(spat_box2_scaled, -0.5,-0.5)
    park_layer = data_source.ExecuteSQL(
        sql_park,        # ogr.CreateGeometryFromWkt(to_wkt(spat_box))
    )
    # spat_box = box(-3.76, 40.36, -3.72, 40.4)
    # spat_box_scaled = affinity.scale(spat_box, group_scale, group_scale)
    scale=500
    polys=[]
    for f in park_layer:
        geo_json = f.ExportToJson()
        fgj=from_geojson(geo_json)
        if(is_valid(fgj)==True):
            polys.append(fgj)
            # print(fgj)
    polys.append(point_buff)
    mp=MultiPolygon(polys)    
    scaled_poly = affinity.scale(
        mp,
        scale,scale
        )
    # f=water_layer.GetExtent()
    features_park = Features(park_layer, item_scale, group_scale)
    # features_water = Features(water_layer, item_scale, group_scale)
    svg_tag = SVGTag(styles)
    svg_tag.prepend(spat_box2_scaled.svg())
    # svg_tag.append(p.svg(), 'extent-level-1')
    # svg_tag.append(point_buff.svg(),'target_area')
    svg_tag.append(scaled_poly.svg(), 'extent-level-2')
    return svg_tag.render()
