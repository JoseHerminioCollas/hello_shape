import os
from madrid_parks import madrid_parks
from madrid_buildings import madrid_buildings

if ('DATA_PATH' not in os.environ.keys()
        or 'FILE_DESTINATION' not in os.environ.keys()):
    print('Error: Environmental Variables not defined')
    exit()

calls = [
    {
        'path':
            os.environ['DATA_PATH'],
        'sql':
            "SELECT * FROM natural where type='park' and name is not null limit {}"
            .format(200),
        'script': madrid_parks,
        'destination': os.environ.get('FILE_DESTINATION'),
    }
]
for i in range(0, 1):
    print(calls[i])
    path = calls[i]['path']
    sql = calls[i]['sql']
    destination = calls[i]['destination']
    # call the provided function to run the script
    calls[i]['script'](path, sql, destination)
