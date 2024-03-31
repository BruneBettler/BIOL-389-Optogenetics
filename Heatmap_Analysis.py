# Author: Brune Bettler
# March 2024

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import matplotlib.patches as patches

from matplotlib.animation import FuncAnimation


# load array from file
data = np.load('OFFdata.npy')


"""
1.) Description Statistics 
    mean and variance over time
    difference over time
"""

def next_direction(data):
    differences = np.diff(data, axis=2)

    # Initialize an array to hold the most common direction of increase for each grid location
    all_direction = np.zeros([10,10,8,900])

    # Define direction vectors for easy reference
    directions = [(-1, 0),(-1, 1), (0, 1), (1, 1), (1, 0),(1, -1), (0, -1), (-1, -1)]

    # Iterate through each time point and grid location (except edges)
    for t in range(differences.shape[2]):
        for x in range(differences.shape[0]):
            for y in range(differences.shape[1]):
                # Track changes for each direction
                for i, tuple in enumerate(directions):
                    dx = tuple[0]
                    dy = tuple[1]
                    # Calculate neighbor's location
                    nx, ny = x + dx, y + dy

                    if 0 <= nx <= 9 and 0 <= ny <= 9:
                         # Record change for this direction
                        if not np.isnan(differences[nx, ny, t]) and differences[nx, ny, t]  > 0:
                            all_direction[x, y, i, t] = differences[nx, ny, t]

    final_im = np.empty((10, 10), dtype=object)

    sum_directions = np.sum(all_direction, axis=3)
    for i in range(sum_directions.shape[0]):
        for j in range(sum_directions.shape[1]):
            if np.max(sum_directions[i][j]) == 0:
                indices = (np.array([-1]),)
            else:
                max_val = np.max(sum_directions[i][j])
                indices = np.where(sum_directions[i][j] == max_val)


            final_im[i, j] = indices

    np.save('most_common_15OFF.npy', final_im)

    # 'most_common_direction' now holds the most likely direction of increase for each grid location and time point

    '''# 'slopes' now contains the slope for each grid location, indicating the trend over time
    map = sns.heatmap(most_common_direction[0], cmap='viridis', annot=False)
    map.set_title('Most Common Next Direction \n Control: 15 minutes light off')
    map.set_xlabel('X Position')
    map.set_ylabel('Y Position')
    # Remove tick labels
    map.set_xticklabels([])
    map.set_yticklabels([])

    cbar = map.collections[0].colorbar
    cbar.set_label('Next direction', rotation=270, labelpad=15)

    # plt.savefig('Control 15min off Linear regression per location.png')

    plt.show()'''


"""
21.) Correlation Analysis
    Auto-correclation
    Cross-correlation 
"""
def auto_corr(data_matrix_at_grid_location):
    ROI_center_time_series = pd.Series(data_matrix_at_grid_location)
    autocorrelation = [ROI_center_time_series.autocorr(lag) for lag in range(1,50)]

    # Plotting
    plt.plot(autocorrelation)
    plt.title('Autocorrelation over Time')
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.show()

"""
3.) Trend Analysis 
    Linear Regression
    Moving Averages  
"""

def lin_regress(data):
    # Assuming 'data' is your 3D numpy array of shape (10, 10, Time)
    time_points = np.arange(data.shape[2])

    # Placeholder for slopes and intercepts
    slopes = np.zeros((data.shape[0], data.shape[1]))
    intercepts = np.zeros((data.shape[0], data.shape[1]))

    # Perform linear regression for each grid location
    for i in range(data.shape[0]):  # x dimension
        for j in range(data.shape[1]):  # y dimension
            slope, intercept, r_value, p_value, std_err = stats.linregress(time_points, data[i, j, :])
            slopes[i, j] = slope
            intercepts[i, j] = intercept

    # 'slopes' now contains the slope for each grid location, indicating the trend over time
    map = sns.heatmap(slopes, cmap='RdBu', annot=False)
    map.set_title('Linear Regression Slope Per Location \n Control: 15 minutes light off')
    map.set_xlabel('X Position')
    map.set_ylabel('Y Position')
    # Remove tick labels
    map.set_xticklabels([])
    map.set_yticklabels([])

    cbar = map.collections[0].colorbar
    cbar.set_label('Slope value', rotation=270, labelpad=15)

    # List of grid cells to black out, specified as (x, y) tuples
    blackout_cells = [(0, 0), (0, 1), (1, 0), (0, 8), (0, 9), (1, 9), (8, 9), (9, 9), (9, 8), (8, 0), (9, 1), (9, 0)]

    # Add black rectangles for each cell you want to black out
    for x in range(10):
        for y in range(10):
            cell = (x, y)
            if cell in blackout_cells:
                rect = patches.Rectangle(cell, 1, 1, linewidth=0, edgecolor='none', facecolor='black')
            #else:
                #rect = patches.Rectangle(cell, 1, 1, linewidth=0, edgecolor='none', facecolor='gray', alpha=0.2)
            map.add_patch(rect)

    #plt.savefig('OFF ~ 15 light OFF Linear regression per location.png')

    #plt.show()
"""
4.) Fourier Analysis 
    Fourier transform  
"""

"""
5.) Cluster Analysis 
    Time series clustering   
"""

"""
6.) Dimensionality Reduction 
    PCA   
"""

lin_regress(data)
