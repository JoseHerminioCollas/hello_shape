from Features import Features

svg_text = '<text   x="{}" y="{}" fill="{}" stroke="none" text-anchor="middle">{}</text>'


def madrid_parks(
        layer,
        item_scale=3,
        group_scale=1000,
        font_size=5
):
    features = Features(layer, item_scale, group_scale)
    svg = ''
    for i in range(0, len(features.data)):
        svg += features.scaled_group.geoms[i].svg()
        svg += ('<text   x="{}" y="{}" text-anchor="middle">{}</text>'
        .format(
            features.scaled_group.geoms[i].centroid.x,
            features.scaled_group.geoms[i].centroid.y,
            features.data[i]['properties']['name']
        ))
    return svg
