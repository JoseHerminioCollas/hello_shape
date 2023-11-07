import json
from shapely import from_geojson, affinity, MultiPolygon


class Features:
    def __init__(
            self,
            layer,
            item_scale=1,
            group_scale=1000):
        self.item_scale = item_scale
        self.group_scale = group_scale
        self.data = []
        self.polygons = []
        self.scaled = []
        [self.add_feature(feature)
         for feature in layer]
        self.scaled_group = affinity.scale(
            MultiPolygon(self.scaled),
            self.group_scale,
            -self.group_scale)

    def add_feature(self, feature):
        geo_json = feature.ExportToJson(True)
        self.data.append(geo_json)
        self.polygons.append(from_geojson(json.dumps(geo_json)))
        scaled_poly = affinity.scale(from_geojson(json.dumps(geo_json)),
                                     self.item_scale, self.item_scale)
        self.scaled.append(scaled_poly)
        return True

    def print_info(self):
        for p in self.data:
            print(p['properties'])
