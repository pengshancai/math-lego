# Author: Pengshan Cai
# Email: pengshancai@umass.edu

from lego_basic import paint_const, paint_linear
from utils import *

# prepare the paper
plt.figure(num='Math Lego')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('The Fish')
delta = 0.0

angle1 = 45
angle2 = -45
line_width = 9
x0 = (0.1, 0.5)
x_eye = (0.23, 0.55)
color1 = 'red'
color2 = 'yellow'

args = {
    'x': x0,
    'angle': angle1,
    'color': color1,
    'num_steps': 125,
    'init_bend_rate': 0,
    'target_bend_rate': 0.6,
    'step_size': 0.003,
    'line_width': (1, line_width),
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

args = {
    'x': x,
    'angle': angle,
    'color': color1,
    'num_steps': 50,
    'bend_rate': bend_rate,
    'step_size': 0.003,
    'line_width': line_width,
    'delta': delta
}
x, angle, bend_rate = paint_const(args)

args = {
    'x': x,
    'angle': angle,
    'color': color1,
    'num_steps': 150,
    'init_bend_rate': bend_rate,
    'target_bend_rate': -0.3,
    'step_size': 0.003,
    'line_width': (line_width, 1),
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

args = {
    'x': x0,
    'angle': angle2,
    'color': color2,
    'num_steps': 125,
    'init_bend_rate': 0,
    'target_bend_rate': -0.6,
    'step_size': 0.003,
    'line_width': (1, line_width),
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

args = {
    'x': x,
    'angle': angle,
    'color': color2,
    'num_steps': 50,
    'bend_rate': bend_rate,
    'step_size': 0.003,
    'line_width': line_width,
    'delta': delta
}
x, angle, bend_rate = paint_const(args)

args = {
    'x': x,
    'angle': angle,
    'color': color2,
    'num_steps': 150,
    'init_bend_rate': bend_rate,
    'target_bend_rate': 0.3,
    'step_size': 0.003,
    'line_width': (line_width, 1),
    'delta': delta
}
x, angle, bend_rate = paint_linear(args)

# paint fish point eye
args = {
    'x': x_eye,
    'angle': 90,
    'color': (0.0, 0.0, 0.0, 0.1),
    'num_steps': 60,
    'bend_rate': 15,
    'step_size': 0.003,
    'line_width': 3,
    'delta': delta
}
x, angle, bend_rate = paint_const(args)

plt.show()