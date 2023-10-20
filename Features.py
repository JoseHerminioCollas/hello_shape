class Features:
 def __init__(self, layer):
  self.data=[feature.ExportToJson(True) for feature in layer]
 polygons=[]
 multi_polygon=[]
 multi_polygon_scaled=[]
