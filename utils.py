# Author: Pengshan Cai
# Email: pengshancai@umass.edu

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time

# Transform an angle to radian
def angle2radian(angle):
    return angle/180 * np.pi

def radian2angle(radian):
    return radian * 180/np.pi

# given a current point, an angle and step size, get the next point
def get_next_point(x, angle, step_size):
    y = np.zeros(2)
    y[0] = x[0] + step_size * np.cos(angle2radian(angle))
    y[1] = x[1] + step_size * np.sin(angle2radian(angle))
    return y

def point_transform(x, y):
    assert len(x) == 2 and len(y) == 2
    x1 = np.array([x[0], y[0]])
    x2 = np.array([x[1], y[1]])
    return x1, x2

def animate(x, y, color=(0.0, 0.0, 0.3, 1.0), line_width=2):
    x1, x2 = point_transform(x, y)
    df=pd.DataFrame({'x1': x1, 'x2': x2})
    plt.plot('x1', 'x2', data=df,  color=color, linewidth=line_width)
    plt.plot()
    # time.sleep(delta)

def get_color(color, num_steps):
    if type(color) == str:
        for i in range(num_steps):
            yield color
    elif len(color) == 4:
        for i in range(num_steps):
            yield color
    else:
        assert len(color) == 2
        assert len(color[0]) == len(color[1])
        assert len(color[0]) == 4
        r_range = np.linspace(color[0][0], color[1][0], num_steps)
        g_range = np.linspace(color[0][1], color[1][1], num_steps)
        b_range = np.linspace(color[0][2], color[1][2], num_steps)
        a_range = np.linspace(color[0][3], color[1][3], num_steps)
        for i in range(num_steps):
            yield (r_range[i], g_range[i], b_range[i], a_range[i])

def get_line_width(line_width, num_steps):
    if type(line_width) == float or type(line_width) == int:
        for i in range(num_steps):
            yield line_width
    else:
        assert len(line_width) == 2
        line_width_range = np.linspace(line_width[0], line_width[1], num_steps)
        for i in range(num_steps):
            yield line_width_range[i]





