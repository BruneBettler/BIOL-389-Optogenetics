# created March 2024
# Author: Brune Bettler

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('dataHEATMAP.csv') # made for control 15 off

# column info: column 1
# row info: column 0
# IN (seconds)
# OUT (seconds)

# for PPK control 1: MAX = 225 seconds (3m 45s)

# 10x10 grid over 225 seconds
heatmap = np.zeros((10, 10, 226))
average_heatmap = np.zeros((10, 10))

# row by column

'''
DOCUMENT INFO
'''
start_row = 2
end_row = 525

c_start_sec = 5
c_end_sec = 6

currentHEAT_x = 0
currentHEAT_y = 0

for data_row in range(start_row, end_row+1):
    # check if the heatmap grid is indicated (signals the start of a new grid location)
    if not pd.isna(data.iloc[data_row, 0]):
        currentHEAT_x = int(data.iloc[data_row, 0]) - 1
        currentHEAT_y = int(data.iloc[data_row, 1]) - 1
        average_heatmap[currentHEAT_x, currentHEAT_y] = round(float(data.iloc[data_row, 10]), 2)

    # fill the heatmap array using sec info from column 5 & 6
    entry_time = int(data.iloc[data_row, 5])
    exit_time = int(data.iloc[data_row, 6])

    if entry_time != -1:
        for sec in range(entry_time, exit_time+1):
            heatmap[currentHEAT_x, currentHEAT_y, sec] += 1

    else:
        heatmap[currentHEAT_x, currentHEAT_y, :] = np.NaN


"""# Generate the heatmap
summed_over_time = np.sum(heatmap, axis=2)

map = sns.heatmap(summed_over_time, cmap='viridis', annot=False)
map.set_title('Total Larval Entries in Space Summed Over Time \n Control: 15 minutes light off')
map.set_xlabel('X Position')
map.set_ylabel('Y Position')
# Remove tick labels
map.set_xticklabels([])
map.set_yticklabels([])

cbar = map.collections[0].colorbar
cbar.set_label('Total Number of Entries', rotation=270, labelpad=15)

plt.savefig('Control 15on Heatmap Entries Summmed Over Time.png')

plt.show()

'''
average heatmap
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

map = sns.heatmap(average_heatmap, cmap='viridis', annot=False)
map.set_title('Pass-Through or Event Locations \n Average Length of Larval Entries in Space \n Control: 15 minutes light off')
map.set_xlabel('X Position')
map.set_ylabel('Y Position')
# Remove tick labels
map.set_xticklabels([])
map.set_yticklabels([])

plt.savefig('Control 15on Heatmap Average Length of Entries ~~ pass or stay location.png')

plt.show()"""








