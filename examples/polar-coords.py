import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

# Example Python Program to plot a polar plot of a circle

# import the numpy and pyplot modules
import numpy as np
import matplotlib.pyplot as plot

plot.axes(projection='polar')

# Set the title of the polar plot
plot.title('Circle in polar format:r=R')

# Plot a circle with radius 2 using polar form
rads = np.arange(0, (2*np.pi), 0.01)

for radian in rads:
    plot.polar(radian,2,'o')

# Display the Polar plot
plot.show()