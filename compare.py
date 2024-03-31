# created March 08 2024
# Author: Brune Bettler

import pandas as pd
from scipy.stats import mannwhitneyu
import numpy as np

data = pd.read_csv('dataROI.csv')

C = (18,22)
D = (25,30)

D_red = [] #
R1 = []
R2 = []
R3 = []
D_white = [] #

columns = (0,29)

experiments = [C]

y_row = 0

for ex_id, experiment in enumerate(experiments):
    start_row = experiment[0]
    end_row = experiment[1]

    # iterate through the different larva
    for larva_id, larva_column in enumerate(range(columns[0], columns[1], 2)):
        # plot the larvae entry and exit times in the correct row
        y_row += 1
        if larva_id == 8 or larva_id == 14:
            continue

        # iterate through the different entries
        for entry_row in range(start_row, end_row + 1):

            start_time = round(float(data.iloc[entry_row, larva_column]), 2)
            if start_time == -1 or pd.isna(start_time):
                break
            if start_time == 0:
                '''D_red.append(0)
                D_white.append(0)
                R1.append(0)
                R2.append(0)
                R3.append(0)'''
                break

            end_time = round(float(data.iloc[entry_row, larva_column + 1]), 2)

            if 0 <= start_time < 300:
                D_red.append(end_time - start_time)
                R1.append(end_time - start_time)
            elif 600 <= start_time < 900:
                D_red.append(end_time - start_time)
                R2.append(end_time - start_time)
            elif 1200 <= start_time < 1500:
                D_red.append(end_time - start_time)
                R3.append(end_time - start_time)
            else:
                D_white.append(end_time - start_time)

R1 = np.array(R1)
R2 = np.array(R2)
R3 = np.array(R3)
D_red = np.array(D_red)
D_white = np.array(D_white)

print('D_red:')
print(D_red)
print('mean')
print(np.mean(D_red))
print('norm sum')
print(np.sum(D_red) / (900*13))
print('list len')
print(len(D_red))

print('D_white:')
print(D_white)
print('mean')
print(np.mean(D_white))
print('norm sum')
print(np.sum(D_white) / (900*13))
print('list len')
print(len(D_white))

stat, p = mannwhitneyu(D_red, D_white)

print(stat)
print(p)

print('R1:')
print(R1)
print('mean')
print(np.mean(R1))
print(' sum')
print(np.sum(R1) / (300*13))
print('list len')
print(len(R1))

print('R2:')
print(R2)
print('mean')
print(np.mean([0]))
print(' sum')
print(np.sum(R2) / (300*13))
print('list len')
print(len(R2))

print('R3:')
print(R3)
print('mean')
print(np.mean(R3))
print(' sum')
print(np.sum(R3) / (300*13))
print('list len')
print(len(R3))

stat, p = mannwhitneyu(R1, R3)








