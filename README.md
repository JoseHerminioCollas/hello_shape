# Geospatial SVG

## Description

This repository attempts to establish strategies for generating SVG files representing Geospatial data.
The technologies used will be primarily: 

* GDAL
* Shapely
* Python

GDAL for accessing data from various sources. Shapely for the creation and modification of geo data.
Python is the scripting language that puts it all together and will be running the commands.

The current strategy makes use of two custom Python classes:

### Features
A class to store data and Shapely objects created from the data.

### SVGTag
A class that is built out from an instance of the Features class. This class renders a final SVG document that is written to disk.

### Scripts

Scripts that run the commands to process the data and write the file. 
Configuration is stored as a path to the data, and SQL command to retreive data and a Python function to do the work.

### Run tests with pytest

## Install

These Python scripts uses several libraries.

### shapely 

https://pypi.org/project/shapely/

###  GDAL

https://gdal.org/

https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html

https://pcjericks.github.io/py-gdalogr-cookbook/

### pytest

https://docs.pytest.org/en/7.4.x/


### Data Source

The following are links to data sources used in this project.

#### Natural Earth

https://www.naturalearthdata.com/

https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/


## Other Related Links

https://mapscaping.com/how-to-read-a-shapefile-using-python/

https://shapely.readthedocs.io

https://catalog.data.gov/dataset/?metadata_type=geospatial&vocab_category_all=Water

https://www.learndatasci.com/tutorials/geospatial-data-python-geopandas-shapely/

https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

https://www.geopackage.org/

https://docs.qgis.org/

https://libgeos.org/

https://en.wikipedia.org/wiki/Geographic_coordinate_conversion#From_geodetic_to_ECEF_coordinates

https://en.wikipedia.org/wiki/Geodetic_datum#World_Geodetic_System_1984_(WGS_84)