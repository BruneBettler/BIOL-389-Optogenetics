# created March 2024
# Author: Brune Bettler

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.patches as patches

# made for control 15 minutes on data
data = pd.read_csv('data15.csv')

# column info: column 1
# row info: column 0
# IN (seconds)
# OUT (seconds)

# for 15 light on 1: MAX = 900 seconds

# 10x10 grid over 225 seconds
heatmap = np.zeros((10, 10, 901))
sum_map = np.zeros((10,10))
mean_map = np.zeros((10,10))

'''
DOCUMENT INFO
'''
start_row = 1
end_row = 513

c_start_sec = 11
c_end_sec = 12

currentHEAT_x = 0
currentHEAT_y = 0

for data_row in range(start_row, end_row+1):
    # check if the heatmap grid is indicated (signals the start of a new grid location)
    if not pd.isna(data.iloc[data_row, 0]):
        currentHEAT_x = int(data.iloc[data_row, 0]) - 1
        currentHEAT_y = int(data.iloc[data_row, 1]) - 1
        mean_map[currentHEAT_x, currentHEAT_y] = round(float(data.iloc[data_row, 16]), 2)


    # fill the heatmap array using sec info from column 5 & 6
    entry_time = round(float(data.iloc[data_row, c_start_sec]))
    exit_time = round(float(data.iloc[data_row, c_end_sec]))

    if entry_time != -1:
        for sec in range(entry_time, exit_time+1):
            heatmap[currentHEAT_x, currentHEAT_y, sec] = 1
        sum_map[currentHEAT_x, currentHEAT_y] += 1

    else:
        heatmap[currentHEAT_x, currentHEAT_y, :] = np.NaN

#np.save('mean_map_ON.npy', mean_map)

#np.save('OFFdata.npy', heatmap)
# Generate the heatmap
summed_over_time = np.sum(heatmap, axis=2) # total number of seconds in which worm was in location
percent_time = summed_over_time / 900

map = sns.heatmap(mean_map, cmap='viridis', annot=False)
map.set_title('Mean Time Spent in Location \n Control: 15 minutes light on')
map.set_xlabel('X Position')
map.set_ylabel('Y Position')
# Remove tick labels
map.set_xticklabels([])
map.set_yticklabels([])

cbar = map.collections[0].colorbar
cbar.set_label('Mean Time in Seconds', rotation=270, labelpad=15)

# List of grid cells to black out, specified as (x, y) tuples
blackout_cells = [(0, 0), (0, 1), (1, 0), (0,8), (0,9), (1,9), (8,9), (9,9),(9,8),(8,0),(9,1),(9,0)]

# Add black rectangles for each cell you want to black out
for x in range(10):
    for y in range(10):
        cell = (x,y)
        if cell in blackout_cells:
            rect = patches.Rectangle(cell, 1, 1, linewidth=0, edgecolor='none', facecolor='white')
        else:
            rect = patches.Rectangle(cell, 1, 1, linewidth=0, edgecolor='none', facecolor='gray', alpha=0.2)
        map.add_patch(rect)



plt.savefig('ON ~ Mean time per location .png')

plt.show()

'''
average heatmap
'''
'''
for x in range(10):
    for y in range(10):
        if average_heatmap[x][y] == -1:
            average_heatmap[x][y] = np.NaN

map = sns.heatmap(average_heatmap, cmap='viridis', annot=False)
map.set_title('Average Length of Larval Entries in Space \n Control: 15 minutes light off')
map.set_xlabel('X Position')
map.set_ylabel('Y Position')
# Remove tick labels
map.set_xticklabels([])
map.set_yticklabels([])

cbar = map.collections[0].colorbar
cbar.set_label('Average Length of Entry (seconds)', rotation=270, labelpad=15)

plt.savefig('Control 15on Heatmap Average Length of Entries.png')

plt.show()
"""
map = sns.heatmap(average_heatmap, cmap='viridis', annot=False)
map.set_title('Pass-Through or Event Locations \n Average Length of Larval Entries in Space \n Control: 15 minutes light off')
map.set_xlabel('X Position')
map.set_ylabel('Y Position')
# Remove tick labels
map.set_xticklabels([])
map.set_yticklabels([])

plt.savefig('Control 15on Heatmap Average Length of Entries ~~ pass or stay location.png')

plt.show()

'''






