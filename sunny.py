# Author: Pengshan Cai
# Email: pengshancai@umass.edu

from lego_basic import paint_linear, paint_const, paint_sin
from utils import *

# prepare the paper
plt.figure(num='Math Lego')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('The Sunny Function')
line_width1 = 9
line_width2 = 7
delta = 0.0

# now let's start painting!

# Part 1
# 0
args = {
    'x': [0.18, 0.33],
    'angle': 96,
    'color': ((1.0, 0.9,  0.0, 0.0), (1.0, 0.9,  0.0, 0.8)),
    'num_steps': 50,
    'bend_rate': 0.1,
    'step_size': 0.0039,
    'line_width': (6, line_width1),
    'delta': delta
}
x, angle, bend_rate = paint_const(args)

# the first line
args = {
    'x': x,
    'angle': angle,
    'color': (1.0, 0.9,  0.0, 0.8),
    'num_steps': 18,
    'bend_rate': 0.1,
    'step_size': 0.0039,
    'line_width': line_width1,
    'delta': delta
}
x, angle, bend_rate = paint_const(args)

# the second line
args = {
    'x': x,
    'angle': angle,
    'color': (1.0, 0.9,  0.0, 0.8),
    'num_steps': 75,
    'init_bend_rate': 0.1,
    'amplitude': 2.8,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 2,
    'step_size': 0.003,
    'line_width': line_width1,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# the third line
args = {
    'x': x,
    'angle': angle,
    # 'color': ((0.0, 0.0, 0.3, 0.5), (0.7, 0.3, 0.0, 0.5)),
    'color': (1.0, 0.9,  0.0, 0.8),
    'num_steps': 25,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 0.27,
    'step_size': 0.003,
    'line_width': line_width1,
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

# 4
args = {
    'x': x,
    'angle': angle,
    'color': (1.0, 0.9,  0.0, 0.8),
    'num_steps': 39,
    'bend_rate': 0.21,
    'step_size': 0.003,
    'line_width': line_width1,
    'delta': delta
}
x, angle, bend_rate = paint_const(args)

# 5
args = {
    'x': x,
    'angle': angle,
    'color': (1.0, 0.9,  0.0, 0.8),
    'num_steps': 18,
    'init_bend_rate': bend_rate,
    'target_bend_rate': bend_rate + 5.1 * np.sin(angle2radian(60)),
    'step_size': 0.003,
    'line_width': line_width1,
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

# 6
args = {
    'x': x,
    'angle': angle,
    'color': (1.0, 0.9,  0.0, 0.8),
    'num_steps': 30,
    'init_bend_rate': bend_rate,
    'amplitude': 0.1,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 6,
    'step_size': 0.003,
    'line_width': line_width1,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# 7
args = {
    'x': x,
    'angle': angle,
    'color': (1.0, 0.9,  0.0, 0.8),
    'num_steps': 10,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 0.2,
    'step_size': 0.003,
    'line_width': line_width1,
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

# 8
args = {
    'x': x,
    'angle': angle,
    'color': ((1.0, 0.9,  0.0, 0.8), (1.0, 0.9,  0.0, 0.3)),
    'num_steps': 189,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 0.06,
    'step_size': 0.003,
    'line_width': (line_width1, 6),
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

# 9
args = {
    'x': x,
    'angle': angle,
    'color': ((1.0, 0.9,  0.0, 0.3), (1.0, 0.9,  0.0, 0.0)),
    'num_steps': 51,
    'bend_rate': bend_rate,
    'step_size': 0.003,
    'line_width': (6, 3),
    'delta': delta
}
x, angle, bend_rate = paint_const(args)

# Part 2
# 1
args = {
    'x': [0.60, 0.90],
    'angle': -87,
    'color': ((0.53, 0.81, 0.92, 0.3), (0.53, 0.81, 0.92, 0.8)),
    'num_steps': 90,
    'init_bend_rate': 0,
    'target_bend_rate': 0.5,
    'step_size': 0.003,
    'line_width': (5, line_width2),
    'delta': 0.001
}
x, angle, bend_rate = paint_linear(args)

# 2
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 30,
    'init_bend_rate': bend_rate,
    'amplitude': 10.5,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 6,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# 3
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 45,
    'init_bend_rate': bend_rate,
    'amplitude': 1.65,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 180/45,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# 4
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 21,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 1.0,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': 0.001
}
x, angle, bend_rate = paint_linear(args)

# 4+
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 29,
    'bend_rate': 1.0,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': 0.001
}
x, angle, bend_rate = paint_const(args)

# 5
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 21,
    'init_bend_rate': bend_rate,
    'amplitude': 12.0,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 180/21,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# 6
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 21,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 1.5,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': 0.001
}
x, angle, bend_rate = paint_linear(args)

# 7
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 30,
    'init_bend_rate': bend_rate,
    'amplitude': 1.8,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 180/30,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# 8
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 27,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 1.0,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': 0.001
}
x, angle, bend_rate = paint_linear(args)

# 8+
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 30,
    'bend_rate': 1.0,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': 0.001
}
x, angle, bend_rate = paint_const(args)

# 9
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 21,
    'init_bend_rate': bend_rate,
    'amplitude': 11.0,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 180/21,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# 10
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 18,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 1.35,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': 0.001
}
x, angle, bend_rate = paint_linear(args)

# 11
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 51,
    'init_bend_rate': bend_rate,
    'amplitude': 0.9,
    'bend_rate_angle': 0,
    'bend_rate_angle_ss': 180/51,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': delta
}
x, angle, bend_rate = paint_sin(args)

# 12
args = {
    'x': x,
    'angle': angle,
    'color': (0.53, 0.81, 0.92, 0.8),
    'num_steps': 35,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 0.8,
    'step_size': 0.003,
    'line_width': line_width2,
    'delta': 0.001
}
x, angle, bend_rate = paint_linear(args)

# 13
args = {
    'x': x,
    'angle': angle,
    'color': ((0.53, 0.81, 0.92, 0.8), (0.53, 0.81, 0.92, 0.1)),
    'num_steps': 69,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 0.1,
    'step_size': 0.003,
    'line_width': (line_width2, 1),
    'delta': 0.001
}
x, angle, bend_rate = paint_linear(args)

plt.show()