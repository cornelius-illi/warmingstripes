#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

## get data from file
## this one is from dwd, and edited a little to be read with numpy
## https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/air_temperature_mean/regional_averages_tm_year.txt
## skip 2 header rows, select last column "Germany" only
data = np.loadtxt("regional_averages_tm_year_1985-2019.txt", delimiter=';', skiprows=2, usecols=(18))
stacked_temps = np.stack((data, data))

vmin = 6.5
vmax = 11.2
## plotting
###############
plt.figure(figsize=(10,10))
img = plt.imshow(stacked_temps, cmap='RdBu_r', aspect=12, vmin=vmin, vmax=vmax)
#img = plt.imshow(stacked_temps, cmap='RdBu_r', aspect=40)

plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0,
            hspace = 0, wspace = 0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.savefig("stripes_germany_1985-2019.png", bbox_inches = 'tight',
    pad_inches = 0, dpi=400)

