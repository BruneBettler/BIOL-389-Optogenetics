# created March 08 2024
# Author: Brune Bettler

import pandas as pd
import matplotlib.pyplot as plt

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
colors = [gray_colors, gray_colors, red_orange_colors, blue_green_colors]

y_row = 0

for ex_id, experiment in enumerate(experiments):
    start_row = experiment[0]
    end_row = experiment[1]

    # iterate through the different larva
    for larva_id, larva_column in enumerate(range(columns[0], columns[1], 2)):
        # plot the larvae entry and exit times in the correct row
        y_row += 1

        # iterate through the different entries
        for entry_row in range(start_row, end_row + 1):

            start_time = round(float(data.iloc[entry_row, larva_column]), 2)
            if start_time == -1:
                break
            end_time = round(float(data.iloc[entry_row, larva_column + 1]), 2)
            if pd.isna(start_time):  # if nan or empty
                break
            plt.plot([start_time, end_time], [y_row, y_row], color=colors[ex_id][larva_id], lw=3)  # could add label: label=('Larva ' + str(larva_num+1))

plt.xlabel('Time (seconds)')
plt.ylabel('ROI Entries per Larva')
plt.gca().set_yticklabels([])
plt.gca().set_yticks(range(1,61))
plt.gca().set_xlim(left=0)
plt.gca().set_xlim(right=1800)
plt.gca().set_ylim(top=61)
plt.gca().set_ylim(bottom=.5)
plt.axhline(y=15, color='black', linestyle=':')
plt.axhline(y=30, color='black', linestyle=':')
plt.axhline(y=45, color='black', linestyle=':')

plt.fill_between(x=[910, 1800], y1=0, y2=15, color='black')
plt.fill_between(x=[1210, 1800], y1=15, y2=30, color='black')
plt.fill_between(x=[1450, 1800], y1=30, y2=45, color='black')

plt.fill_between(x=[0, 900], y1=15, y2=30, color='#FFCCCC', alpha=0.5)

plt.fill_between(x=[0, 300], y1=30, y2=45, color='#FFCCCC', alpha=0.5)
plt.fill_between(x=[420, 720], y1=30, y2=45, color='#FFCCCC', alpha=0.5)
plt.fill_between(x=[840, 1140], y1=30, y2=45, color='#FFCCCC', alpha=0.5)

plt.fill_between(x=[0, 300], y1=45, y2=61, color='#FFCCCC', alpha=0.5)
plt.fill_between(x=[600, 900], y1=45, y2=61, color='#FFCCCC', alpha=0.5)
plt.fill_between(x=[1200, 1500], y1=45, y2=61, color='#FFCCCC', alpha=0.5)

plt.suptitle('All conditions', fontsize=10)  # Adding a subtitle
plt.title('ROI Visits Over Time Per Larva')


plt.tight_layout()

plt.savefig('Test ~ All conditions.png')  # Saves the plot as a PNG file

plt.show()


