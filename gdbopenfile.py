# from osgeo import ogr
# point = ogr.Geometry(ogr.wkbPoint)
# point.AddPoint(1198054.34, 648493.09)
# print( point.ExportToWkt())

from osgeo import ogr

geojson = """{"type":"Point","coordinates":[108420.33,753808.59]}"""
point = ogr.CreateGeometryFromJson(geojson)
print ("%d,%d" % (point.GetX(), point.GetY()))