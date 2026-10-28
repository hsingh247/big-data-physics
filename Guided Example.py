# Welcome to the guided example!
# Your task is to create a pressure vs. altitude plot for a launch of your choosing
# Remember to save any files as .csv files

# ---------------------------------------------------------------------------------

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Main loop for reading data
cw = "Annafy_DF_1PA025.csv"

######################################
## Altitude vs Time
######################################

# altitudes = []
# times = []
# # Keep only the ascent, including the highest point
# with open(cw) as file:
#     lines = file.readlines()
#     for line in lines[1:]:
#         data = line.split(",")
#         alt = float(data[7])
#         altitudes.append(alt)
#         time = datetime.strptime(data[4], '%H:%M:%S.%f')
#         times.append(time)

# # Create the Plot
# plt.plot(times, altitudes, 'o', markersize=3)
# plt.title("05/31/2025 Launch Altitude Data")
# plt.xlabel("Time")
# plt.ylabel("Altitude")
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
# plt.show()

######################################
## Pressure vs Altitude
######################################
        
altitudes = []
pressures = []
# Keep only the ascent, including the highest point
with open(cw) as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.split(",")
        alt = float(data[7])
        altitudes.append(alt)
        pressure = float(data[2])
        pressures.append(pressure)

peak_index = altitudes.index(max(altitudes))

altitudes = altitudes[:peak_index + 1]
pressures = pressures[:peak_index + 1]

# Create the Plot
plt.plot(altitudes, pressures, 'o', markersize=3)
plt.title("11/31/2025 Launch Altitude Data")
plt.xlabel("Altitude")
plt.ylabel("Pressure")
plt.show()