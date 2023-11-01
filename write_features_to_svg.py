from madrid_parks import madrid_parks
from madrid_buildings import madrid_buildings
calls=[
{
 'path':
  'data/Madrid-shp/shape/natural.shp',
 'sql':
  "SELECT * FROM natural where type='park' and name is not null limit {}"
   .format(200),
 'script':madrid_parks,
 'destination':'generated/madrid_parks_2023_11_1.svg'},
 {
  'path':
   'data/Madrid-shp/shape/buildings.shp',
  'sql':
   "SELECT * FROM buildings where name is not null limit {}"
   .format(200),
  'script': madrid_buildings,
  'destination': 'generated/madrid_buildings_2023_11_1.svg'
 }
]
for i in range(0,len(calls)):
 print(calls[i])
 path=calls[i]['path']
 sql=calls[i]['sql']
 destination=calls[i]['destination']
 # call the provided function to run the script
 calls[i]['script'](path,sql,destination)
