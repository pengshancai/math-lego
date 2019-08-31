# Author: Pengshan Cai
# Email: pengshancai@umass.edu

from lego_advanced import paint_sunshine
from utils import *

# prepare the paper
plt.figure(num='Math Lego')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('The Sun')
delta = 0.0

x0 = (0.5, 0.5)
w = 0.15
divide = 10
section = 360/divide
colors = ['aquamarine', (1.0, 0.9, 0.05, 0.5), 'lightgreen', 'lavender', 'pink', 'orange', 'wheat', 'yellowgreen', 'lightblue', 'tomato']

for i in range(divide):
    x = (x0[0] + w * np.cos(angle2radian(i * section)), x0[1] + w * np.sin(angle2radian(i * section)))
    # print(x)
    args = {
        'x': x,
        'angle': i * section,
        'color': colors[i]
    }
    _, angle, bend_rate = paint_sunshine(args)

plt.show()