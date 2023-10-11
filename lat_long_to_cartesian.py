# Converting latitude and longitude to cartesian grid values
# https://en.wikipedia.org/wiki/Geographic_coordinate_conversion#From_geodetic_to_ECEF_coordinates
# https://en.wikipedia.org/wiki/Geodetic_datum#World_Geodetic_System_1984_(WGS_84)
import numpy as np

def get_cartesian(latitude=None,longitude=None):
    latitude_rad, longitude_rad = np.deg2rad(latitude), np.deg2rad(longitude)
    # r : radius of earth in aproximate kilometers
    r = 6738
    x = r * np.cos(latitude_rad) * np.cos(longitude_rad)
    y = r * np.cos(latitude_rad) * np.sin(longitude_rad)
    return x,y