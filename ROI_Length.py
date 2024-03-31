# created March 2024
# Author: Brune Bettler

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = pd.read_csv('dataROI.csv')

'''
15 min off data row = 2 -> 9
15 min on 5 off data = 12 ->15
5 on 5 off = 18 -> 22
5 on 2 off = 25 - 30 
'''
A = (2,9)
B = (12,15)
C = (18,22)
D = (25,30)

columns = (0,29)

# iterate through each experiment and add to a graph :)
experiments = [A, B, D, C]

#plt.figure(figsize=(12,10))
blue_green_colors = ['#0D47A1', '#1976D2', '#039BE5', '#00ACC1', '#00897B', '#26A69A', '#4DB6AC', '#80CBC4', '#B2DFDB', '#E0F2F1', '#006064', '#00796B', '#00838F', '#0097A7', '#008D9D']
red_orange_colors = ['#D32F2F', '#E53935', '#F44336', '#FF5722', '#FF7043', '#FF8A65', '#FFA726', '#FFB74D', '#FFCC80', '#FFD54F', '#FFE082', '#FFECB3', '#FFAB91', '#FFCCBC']
gray_colors = ['#B0B0B0', '#A6A6A6', '#9C9C9C', '#929292', '#888888', '#7E7E7E', '#747474', '#6A6A6A', '#606060', '#565656', '#4C4C4C', '#424242', '#383838', '#2E2E2E', '#242424']
colors = [gray_colors, red_orange_colors, blue_green_colors]

"""
'''
FOR Box and whisker plot A,B 
'''
experiments = [A,B]
colors = ['black', 'red']
y_row = 0
experiment_data = []

for ex_id, experiment in enumerate(experiments):
    time_spent = []
    b_over_time = []
    start_row = experiment[0]
    end_row = experiment[1]

    # iterate through the different larva
    for larva_id, larva_column in enumerate(range(columns[0], columns[1], 2)):
        # plot the larvae entry and exit times in the correct row
        y_row += 1
        # iterate through the different entries
        for entry_row in range(start_row, end_row + 1):

            start_time = round(float(data.iloc[entry_row, larva_column]), 2)
            end_time = round(float(data.iloc[entry_row, larva_column + 1]), 2)

            # for experiment B, ignore the times when the larvae had no light on them
            if start_time > 900:
                time_in_roi = end_time - start_time
                b_over_time.append(time_in_roi)
                break

            if pd.isna(start_time) or start_time == -1:  # if nan/empty
                break
            else:
                time_in_roi = end_time - start_time
                time_spent.append(time_in_roi)

    experiment_data.append(time_spent)
    if len(b_over_time) != 0:
        experiment_data.append(b_over_time)

plt.figure(figsize=(7, 8))
plt.boxplot(experiment_data)

# Adding titles and labels
plt.title('Time Spent Per Entry in ROI')
plt.suptitle('Both controls', fontsize=10)  # Adding a subtitle
plt.ylabel('Time of ROI Stays (sec)')
plt.xticks([1, 2, 3], ['15 minutes light off', '15 minutes light on', '5 min light off \n post 15 minutes light on'])
plt.tight_layout()

# plt.savefig('Box and Whisker: ROI Length of Stay: Both controls.png')  # Saves the plot as a PNG file

# Show the plot
plt.show()"""





'''
FOR SCATTERPLOT 
'''
experiments = [A,B]
colors = ['black', 'red']
labels = ['15 minutes light off', '15 minutes light on']
y_row = 0
all_data = []

for ex_id, experiment in enumerate(experiments):
    time_spent = []
    start_row = experiment[0]
    end_row = experiment[1]
    has_been_labeled = False
    exp_data =[]


    # iterate through the different larva
    for larva_id, larva_column in enumerate(range(columns[0], columns[1], 2)):
        # plot the larvae entry and exit times in the correct row
        y_row += 1
        current_larv_entries = []
        L5OFF = []
        # iterate through the different entries
        for entry_row in range(start_row, end_row + 1):

            start_time = round(float(data.iloc[entry_row, larva_column]), 2)
            end_time = round(float(data.iloc[entry_row, larva_column + 1]), 2)

            # for experiment B, ignore the times when the larvae had no light on them
            if start_time > 900:
                time_in_roi = end_time - start_time
                L5OFF.append(time_in_roi)
                continue

            if pd.isna(start_time) or start_time == -1:  # if nan/empty or -1
                break

            time_in_roi = end_time - start_time
            current_larv_entries.append(time_in_roi)

        if len(current_larv_entries) == 0:
            current_larv_entries = [0]

        if len(L5OFF) == 0:
            L5OFF = [0]

        all_entries = np.array(current_larv_entries)
        average_entry_length = np.mean(all_entries)
        average_off = np.mean(np.array(L5OFF))

        if not has_been_labeled:
            plt.scatter(x=(larva_id+1), y=average_entry_length, marker='o', color=colors[ex_id], label=labels[ex_id])
            has_been_labeled = True
        plt.scatter(x=(larva_id + 1), y=average_entry_length, marker='o', color=colors[ex_id])
        #plt.scatter(x=(larva_id + 1), y=average_off, marker='o', color="gray")
        exp_data.append([larva_id + 1, average_entry_length])

    exp_data.pop()
    all_data.append(exp_data)

'''# Fit linear regression models
x1 = [coord[0] for coord in all_data[0]]
y1 = [coord[1] for coord in all_data[0]]
x2 = [coord[0] for coord in all_data[0]]
y2 = [coord[1] for coord in all_data[1]]
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(x1, y1)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x2, y2)'''

# Adding titles and labels
plt.title('Mean Time Spent Per Entry in ROI Per Larva')
plt.suptitle('Both controls', fontsize=10)  # Adding a subtitle
plt.xlabel('Larva ID')
plt.ylabel('Mean Time of ROI Stays (sec)')
plt.gca().set_ylim(bottom=0)
plt.gca().set_xlim(right=14.5)
plt.gca().set_xticks(range(1,15))
plt.tight_layout()
plt.legend()

# Add fitted lines
#plt.plot(x1, intercept1 + slope1*np.array(x1), 'black', label=f'Fit 1: y={slope1:.2f}x+{intercept1:.2f}')
#plt.plot(x2, intercept2 + slope2*np.array(x2), 'red', label=f'Fit 2: y={slope2:.2f}x+{intercept2:.2f}')

#plt.savefig('ROI Length of Stay: Both controls.png')  # Saves the plot as a PNG file

# Show the plot
plt.show()
