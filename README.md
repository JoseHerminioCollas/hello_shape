# Geospatial SVG

<img src="art/geospatial_svg_logo.svg">

## Description

Strategies for generating SVG graphics from Geospatial data.
The technologies used are primarily: GDAL, Shapely, Python and Linux. 

A project by Goatstone, Jose Collas
[goatstone.com](https://goatstone.com)

## Example

A script that generates an SVG of parks and bodies of water in a part of Madrid can produce the following SVG graphic.

<img src="svg_archive/madrid_parks_11_15.svg" width="400" />


The SVGs are generated with the use of a run script, funtion for generating the SVG and two custom Python classes, Features and SVGTag

### Features
A class to store data and Shapely objects created from the data.

### SVGTag
A class that is built out from an instance of the Features class. This class renders a final SVG document that is written to disk.

### Scripts

#### The run script

Scripts that run the commands to process the data and write the file. 

The run script can be thought of as a controller. See the file:

  run_script.py

It runs a function with a name that reflects the kind of graphic it will produce.

The function madrid_natural contains most of the script that will generate an SVG graphic of natural areas in Madrid.


The Process of generating an SVG file is generally as follows:

#### Get the DataSource

#### Get the Layer

#### Build Features objects

#### Write to the SVGObject

#### Call the render method on the instance of SVGObject

#### Write the content of what has been returned by the render method to a file

Graphics can be generated anywhere in the system but saved graphics can be found in the svg_archive folder.


### Run tests with pytest

  pytest

## Install

## Libraries Geospatial SVG uses:

### shapely 

https://pypi.org/project/shapely/

###  GDAL

https://gdal.org/

https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html

https://pcjericks.github.io/py-gdalogr-cookbook/

### pytest

https://docs.pytest.org/en/7.4.x/


### View the SVG graphics.

I have been using primarily Linux for this project. 
On Linux the applications InkScape and ImageViewer work well to view the SVG graphics.

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