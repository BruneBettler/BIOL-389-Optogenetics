# Author: Brune Bettler
# March 2024

import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

import Data.control_15off
import Data.control_15on_5off

def single_larvae_data(session_range_tuple, single_larvae_list):
    # session_range_tuple = (session_start_frame, session_end_frame)
    # single_larvae_data = list of tuples (enter_frame, leave_frame) for each time the larvae enters or exits ROI

    s_start_frame = session_range_tuple[0]
    s_end_frame = session_range_tuple[1]

    larvae_data_time = np.arange(s_start_frame, s_end_frame+1)
    larvae_data_binary = np.arange(s_start_frame, s_end_frame+1)

    curr_tuple_index = 0
    index = 0
    for time_point in range(s_start_frame, s_end_frame+1):
        try:
            curr_tuple = single_larvae_list[curr_tuple_index]
        except:
            curr_tuple = (0,0)
        finally:
            if time_point in range(curr_tuple[0], curr_tuple[1]+1):
                larvae_data_binary[index] = 1
                if time_point == curr_tuple[1]:
                    curr_tuple_index += 1
            else:
                larvae_data_binary[index] = 0
            index += 1

    return larvae_data_time, larvae_data_binary

def grouped_data(session_range_tuple, group_larvae_list):
    # session_range_tuple = (session_start_frame, session_end_frame)
    # single_larvae_data = list of tuples (enter_frame, leave_frame) for each time the larvae enters or exits ROI
    s_start_frame = session_range_tuple[0]
    s_end_frame = session_range_tuple[1]

    x_list = np.arange(s_start_frame, s_end_frame + 1)
    y_list = []
    for larvae_index in range(len(group_larvae_list)):
        larvae_data_binary = np.arange(s_start_frame, s_end_frame + 1)
        curr_tuple_index = 0
        index = 0
        for time_point in range(s_start_frame, s_end_frame + 1):
            try:
                curr_tuple = group_larvae_list[larvae_index][curr_tuple_index]
            except:
                curr_tuple = (0, 0)
            finally:
                if time_point in range(curr_tuple[0], curr_tuple[1] + 1):
                    larvae_data_binary[index] = 1
                    if time_point == curr_tuple[1]:
                        curr_tuple_index += 1
                else:
                    larvae_data_binary[index] = 0
                index += 1
        y_list.append(larvae_data_binary)

    return x_list, y_list

def heatmap(group_y_data):
    heatmap = 0.0
    for larvae_data in group_y_data:
        heatmap += larvae_data

    return heatmap


# 15 min on 5 min off
A_x_data, A_y_data = grouped_data((3088, 21327), Data.control_15on_5off.a_larvae_data)
a_heatmap = heatmap(A_y_data)
plt.plot(A_x_data, a_heatmap)
plt.axvline(x = 16731, color = 'b', label = 'axvline - full height')
plt.show()

B_x_data, B_y_data = grouped_data((2886, 20991), Data.control_15on_5off.b_larvae_data)
b_heatmap = heatmap(B_y_data)
plt.plot(B_x_data, b_heatmap)
plt.axvline(x = 16435, color = 'b', label = 'axvline - full height')
plt.show()









a_x_val, a_y_val = single_larvae_data(Data.control_15off.A_session_frame_range, Data.control_15off.A_worm1_data)
b_x_val, b_y_val = single_larvae_data(Data.control_15off.A_session_frame_range, Data.control_15off.A_worm2_data)
c_x_val, c_y_val = single_larvae_data(Data.control_15off.A_session_frame_range, Data.control_15off.A_worm3_data)
d_x_val, d_y_val = single_larvae_data(Data.control_15off.A_session_frame_range, Data.control_15off.A_worm4_data)
e_x_val, e_y_val = single_larvae_data(Data.control_15off.A_session_frame_range, Data.control_15off.A_worm5_data)
f_x_val, f_y_val = single_larvae_data(Data.control_15off.A_session_frame_range, Data.control_15off.A_worm6_data)
g_x_val, g_y_val = single_larvae_data(Data.control_15off.A_session_frame_range, Data.control_15off.A_worm7_data)

a_heatmap = a_y_val + b_y_val + c_y_val + d_y_val + e_y_val + f_y_val + g_y_val
heatmap = a_heatmap.reshape(1, 18546)


A_x_val, A_y_val = single_larvae_data(Data.control_15off.B_session_frame_range, Data.control_15off.B_worm1_data)
B_x_val, B_y_val = single_larvae_data(Data.control_15off.B_session_frame_range, Data.control_15off.B_worm2_data)
C_x_val, C_y_val = single_larvae_data(Data.control_15off.B_session_frame_range, Data.control_15off.B_worm3_data)
D_x_val, D_y_val = single_larvae_data(Data.control_15off.B_session_frame_range, Data.control_15off.B_worm4_data)
E_x_val, E_y_val = single_larvae_data(Data.control_15off.B_session_frame_range, Data.control_15off.B_worm5_data)
F_x_val, F_y_val = single_larvae_data(Data.control_15off.B_session_frame_range, Data.control_15off.B_worm6_data)
G_x_val, G_y_val = single_larvae_data(Data.control_15off.B_session_frame_range, Data.control_15off.B_worm7_data)

B_heatmap = A_y_val + B_y_val + C_y_val + D_y_val + E_y_val + F_y_val + G_y_val
Heatmap = B_heatmap.reshape(1, 18121)

# show graphs with number of larave in ROI per time step
plt.plot(a_x_val, a_heatmap)
plt.show()

plt.plot(A_x_val, B_heatmap)
plt.show()


'''
# shows a strange heatmap of the amount of worms in the ROI per time step 
hm = sbn.heatmap(data = Heatmap, cmap='gray')
plt.title('Control (15 min light off) Group B')
plt.show()
'''