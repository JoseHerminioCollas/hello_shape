from Features import Features
from SVGTag import SVGTag

def madrid_parks(
        svg_tag,
        layer,
        item_scale=3,
        group_scale=1000,
        font_size=5
):
    features = Features(layer, item_scale, group_scale)
    for i in range(0, len(features.data)):
        svg_tag.set_polygon(features.scaled_group.geoms[i].svg())
        svg_tag.set_text_element(
            features.data[i]['properties']['name'],
            features.scaled_group.geoms[i].centroid.x, features.scaled_group.geoms[i].centroid.y,
            font_size
        )
    return svg_tag
