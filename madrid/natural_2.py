from Features import Features
from SVGTag import SVGTag
from shapely import MultiPolygon, affinity, box, Point, from_geojson,is_valid, to_wkt
from osgeo import ogr

def natural_2(item_scale,group_scale,data_path,styles,spat_zoom=0,center=None):
    sql_park = ("SELECT * FROM natural where type='park' and name is not null limit {}"
        .format(500))
    data_source = ogr.Open(data_path)
    layer=data_source.GetLayer()
    # l1=layer.GetSpatialFilter()
    # spatb = box(0,0,1,1)
    # spat=ogr.CreateGeometryFromWkt(to_wkt(spatb))
    # layer.SetSpatialFilter(spat)
    extent=layer.GetExtent()
    # extent (-4.0699641, -3.2300143, 40.170042, 40.6499669)
    exmidx = extent[0] - ((extent[0] - extent[1]) / 2)
    exmidy=extent[2]-((extent[2]-extent[3])/2)
    print('extent', extent, exmidx)
    p=Point(exmidx,exmidy)
    point_buff=p.buffer(0.1)
    point_bounds=point_buff.bounds
    sbox=box(point_bounds[0],point_bounds[1],point_bounds[2],point_bounds[3])
    spat_box2 = box(extent[0], extent[2], extent[1], extent[3])
    spat_box2_scaled=affinity.scale(spat_box2, group_scale,group_scale)
    park_layer = data_source.ExecuteSQL(
        sql_park,    
         ogr.CreateGeometryFromWkt(to_wkt(sbox))
    )
    scale=500
    polys=[]
    for f in park_layer:
        geo_json = f.ExportToJson()
        fgj=from_geojson(geo_json)
        if(is_valid(fgj)==True):
            polys.append(fgj)
            # print(fgj)
    polys.append(point_buff)
    polys.append(sbox)
    mp=MultiPolygon(polys)    
    scaled_poly = affinity.scale(
        mp,
        scale,scale
        )
    features_park = Features(park_layer, item_scale, group_scale)
    svg_tag = SVGTag(styles)
    svg_tag.prepend(spat_box2_scaled.svg(),'extent-level-1')
    svg_tag.append(sbox.svg(),'target_area')
    svg_tag.append(scaled_poly.svg(), 'extent-level-2')
    return svg_tag.render()
