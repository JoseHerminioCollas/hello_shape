import json


def get_feature_coords(feature):
 featureJSON=feature.ExportToJson()
 featureObj=json.loads(featureJSON)
 # has only one entry because it is a polygon
 return featureObj['geometry']['coordinates'][0]