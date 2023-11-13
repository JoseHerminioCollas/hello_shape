from Features import Features


def layer_to_svg(
        layer,
        item_scale=3,
        group_scale=1000,
):
    features = Features(layer, item_scale, group_scale)
    svg = '<g class="parks">'
    for i in range(0, len(features.data)):
        svg += features.scaled_group.geoms[i].svg()
        svg += ('<text x="{}" y="{}">{}</text>'
        .format(
            features.scaled_group.geoms[i].centroid.x,
            features.scaled_group.geoms[i].centroid.y,
            features.data[i]['properties']['name']
        ))
    svg += '</g>'
    return svg
