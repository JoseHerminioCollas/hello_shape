from shapely import from_geojson,buffer,affinity, MultiPolygon, Polygon, LineString, MultiLineString

# loop through data and make shape objects, scale MultiLineString
def get_text_svg(geo_data,shapes):
 str=''
 for i in range(0,len(geo_data)):
  line_string=LineString(shapes[i])
  s='<text font-size="3" x="{}" y="{}" fill="black" stroke="none">{}</text>'
  str+=s.format(line_string.centroid.x,line_string.centroid.y,geo_data[i]['properties']['name'])

 return str