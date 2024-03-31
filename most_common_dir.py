# Author: Brune Bettler
# March 2024

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def val_to_UV(val):
    if val==0:
        U = 0
        V = .5
    elif val==1:
        U = .5
        V = .5
    elif val ==2:
        U = .5
        V = 0
    elif val ==3:
        U = .5
        V = -.5
    elif val ==4:
        U = 0
        V = -.5
    elif val ==5:
        U = -.5
        V = -.5
    elif val ==6:
        U = -.5
        V = 0
    elif val ==7:
        U = -.5
        V = .5

    return U,V

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))

all_directions = np.load('most_common_15OFF.npy', allow_pickle=True)

x_vals = np.arange(0.5, 10, 1)
y_vals = np.arange(9.5, 0, -1)

X = []
Y = []
U = []
V = []

for np_x in range(10):
    for np_y in range(10):
        for arrow_dir in all_directions[np_y,np_x][0]:
            X.append(x_vals[np_x])
            Y.append(y_vals[np_y])
            if arrow_dir == -1:
                u, v = 0, 0
            else:
                u, v = val_to_UV(arrow_dir)
            U.append(u)
            V.append(v)

ax.quiver(X, Y, U, V, angles='xy', scale=1, scale_units='xy', pivot='tail', headwidth=4, headaxislength=2, headlength=2)

# Set limits and aspect ratio to ensure the grid is square and centered
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Optionally, hide the axes
ax.axis('on')

# List of grid cells to black out, specified as (x, y) tuples
blackout_cells = [(0, 0), (0, 1), (1, 0), (0,8), (0,9), (1,9), (8,9), (9,9),(9,8),(8,0),(9,1),(9,0)] # (9,2)

# Add black rectangles for each cell you want to black out
for x in range(10):
    for y in range(10):
        cell = (x,y)
        if cell in blackout_cells:
            rect = patches.Rectangle(cell, 1, 1, linewidth=0, edgecolor='none', facecolor='white')
        else:
            rect = patches.Rectangle(cell, 1, 1, linewidth=0, edgecolor='none', facecolor='gray', alpha=0.2)
        ax.add_patch(rect)

plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.yticks([1,2,3,4,5,6,7,8,9,10])
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid()
plt.title('Most Common Direction of Movement From One Location to Another \n Control: 15 minutes light off \n')
plt.tight_layout()

plt.savefig('OFF ~ Most common direction ~ control1 15 off.png')
plt.show()
