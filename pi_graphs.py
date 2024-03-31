# Author: Brune Bettler
# March 2024

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = (2, 9)
B = (12, 15)
C = (18, 22)
D = (25, 30)
columns = (0, 29)

def data_prep(experiments, raw_data):
    # output a list containing a list of four numbers per experiment
    # [NL_average_time_in_ROI, NL_average_time_out_ROI, RL_average_time_in_ROI, RL_average_time_out_ROI]

    data = raw_data

    for ex_id, experiment in enumerate(experiments):
        time_spent_norm = []
        b_over_time = []
        start_row = experiment[0]
        end_row = experiment[1]

        # iterate through the different larva

        for larva_id, larva_column in enumerate(range(columns[0], columns[1], 2)):
            larva_total_time = []
            b_larva_total_time = []
            # iterate through the different entries
            for entry_row in range(start_row, end_row + 1):

                start_time = round(float(data.iloc[entry_row, larva_column]), 2)
                end_time = round(float(data.iloc[entry_row, larva_column + 1]), 2)

                # for experiment B, ignore the times when the larvae had no light on them
                if start_time > 900:
                    time_in_roi = end_time - start_time
                    b_larva_total_time.append(time_in_roi)

                if pd.isna(start_time) or start_time == -1:  # if nan/empty
                    break
                else:
                    time_in_roi = end_time - start_time
                    larva_total_time.append(time_in_roi)

            total_time_spent = np.sum(np.array(larva_total_time))
            b_total_time = np.sum(np.array(b_larva_total_time))
            time_spent_norm.append(total_time_spent / 900)
            b_over_time.append(b_total_time / 300)


        if experiment != B:
            time_spent_norm.pop()

        experiment_data15 = np.mean(np.array(time_spent_norm))
        experiment_data5 = np.mean(np.array(b_over_time))

    return experiment_data15, experiment_data5

def make_pi(data, title, titlea, titleb):
    # Data to plot
    labels = ['in ROI', 'out of ROI']
    red_colors = ['lightcoral', (0.753, 0.4, 0.4)]
    gray_colors = ['lightgray', 'darkgray']

    fig = plt.figure(figsize=(10, 5))
    fig.suptitle(title)

    ax1 = fig.add_subplot(121)
    patches, _, _ = ax1.pie(data[0], labels=labels, colors=red_colors, autopct='%1.1f%%', startangle=140,
                            wedgeprops={'edgecolor': 'black', 'linewidth': .4})
    ax1.set_title(titlea)
    ax1.axis('equal')
    patches[0].set_hatch('/')

    ax2 = fig.add_subplot(122)
    patches, _, _ = ax2.pie(data[1], labels=labels, colors=gray_colors, autopct='%1.1f%%', startangle=140,
                            wedgeprops={'edgecolor': 'black', 'linewidth': .4})
    ax2.set_title(titleb)
    ax2.axis('equal')
    patches[0].set_hatch('/')

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()

    #plt.savefig('Two Control PIes.png')  # Saves the plot as a PNG file

    plt.show()

if __name__ == '__main__':
    raw_data = pd.read_csv('dataROI.csv')
    # iterate through each experiment and add to a graph :)

    experiments = [B]

    output15, output5 = data_prep(experiments, raw_data)
    in_output15 = round(output15, 2)
    out_output15 = 1 - in_output15
    in_output5 = round(output5, 2)
    out_output5 = 1 - in_output5
    data = [[in_output15, out_output15], [in_output5, out_output5]]
    make_pi(data, 'Average Total Time Spent per Larva \n Control: 15 min light on + 5 min light off \n n = 15', '15 minutes light on', '5 minutes light off')
