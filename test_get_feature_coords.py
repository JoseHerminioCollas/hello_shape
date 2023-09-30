from get_feature_coords import get_feature_coords

class FeatureMock():
 def ExportToJson(self):
  return '{"geometry":{"coordinates":[[2,2]]}}'
def test_get_feature_coords():
 feature_mock=FeatureMock()
 assert get_feature_coords(feature_mock)==[2,2]