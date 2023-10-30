import json
from shapely import from_geojson,affinity,MultiPolygon
class Features:
 def __init__(self, layer):
  self.item_scale = 1000
  self.group_scale = 1000
  self.data = []
  self.polygons = []
  self.scaled = []
  [self.add_feature(feature)
   for feature in layer]
  self.scaled_group = affinity.scale(
   MultiPolygon(self.polygons),
   self.group_scale,
   self.group_scale)
 def add_feature(self, feature):
  geo_json=feature.ExportToJson(True)
  self.data.append(geo_json)
  self.polygons.append(from_geojson(json.dumps(geo_json)))
  scaled_poly=affinity.scale(from_geojson(json.dumps(geo_json)),
   self.item_scale,self.item_scale)
  self.scaled.append(scaled_poly)
  return  True
