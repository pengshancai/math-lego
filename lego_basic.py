# Author: Pengshan Cai
# Email: pengshancai@umass.edu

from utils import *

delta_min = 1e-17

# the derivative is a constant
def const_bender(args):
    num_steps = args['num_steps']
    cur_angle = args['angle']
    bend_rate = args['bend_rate']
    for i in range(num_steps):
        yield cur_angle, bend_rate
        cur_angle -= bend_rate

# the derivative is in accordance with a linear function
# smoothly adjust the derivative, keeping the function differentiable (thus smooth)
def linear_bender(args):
    num_steps = args['num_steps']
    cur_angle = args['angle']
    bend_rate_ss = (args['target_bend_rate'] - args['init_bend_rate'])/num_steps
    bend_rate = args['init_bend_rate']
    for i in range(num_steps):
        cur_angle -= bend_rate
        bend_rate += bend_rate_ss
        yield cur_angle, bend_rate

# the derivative is in accordance with a sin function
# d_bend_rate_angle_ss: step size of the bend rate angle, increase this parameter would cause a more curly bend
# amplitude: the maximum bend rate derivative, increase this parameter would also cause a more curly bend
def sin_bender(args):
    # parameters
    num_steps = args['num_steps']
    cur_angle = args['angle']
    init_bend_rate = args['init_bend_rate']
    bend_rate = init_bend_rate
    amplitude = args['amplitude']
    bend_rate_angle = args['bend_rate_angle']
    bend_rate_angle_ss = args['bend_rate_angle_ss']
    for i in range(num_steps):
        d_bend_rate = amplitude * np.sin(angle2radian(bend_rate_angle))
        cur_angle -= bend_rate
        bend_rate = init_bend_rate + d_bend_rate
        bend_rate_angle += bend_rate_angle_ss
        yield cur_angle, bend_rate

# slowly decrease to zero
def exp_bender(args):
    pass

# the derivative is in accordance with a inverse function
def inverse_bender():
    pass

# Make sure all necessary parameters are contained in args
# if not, use the default setting
def sanity_check(args):
    assert 'x' in args
    assert 'angle' in args
    if 'color' not in args:
        args['color'] = (1.0, 1.0, 1.0, 1.0)
    if 'num_steps' not in args:
        args['num_steps'] = 180
        print('number of step not specified')
    if 'step_size' not in args:
        args['step_size'] = 0.01
        print('step size not specified')
    if 'line_width' not in args:
        args['line_width'] = 1.0
        print('line width not specified')
    if 'delta' not in args:
        args['delta'] = 0.09

def paint(args, bender):
    x = args['x']
    palette = get_color(args['color'], args['num_steps'])
    line_width_iter = get_line_width(args['line_width'], args['num_steps'])
    for angle, bend_rate in bender:
        y = get_next_point(x, angle, args['step_size'])
        color = next(palette)
        line_width = next(line_width_iter)
        animate(x, y, color, line_width)
        x = y
        plt.draw()
        plt.pause(delta_min)
        time.sleep(args['delta'])
    return x, angle, bend_rate

def paint_const(args):
    # sanity check
    sanity_check(args)
    assert 'bend_rate' in args
    # initialization
    bender = const_bender(args)
    # paint
    return paint(args, bender)

def paint_linear(args):
    # sanity check
    sanity_check(args)
    assert 'init_bend_rate' in args
    assert 'target_bend_rate' in args
    # initialization
    bender = linear_bender(args)
    # paint
    return paint(args, bender)

def paint_sin(args):
    # sanity check
    sanity_check(args)
    assert 'init_bend_rate' in args
    assert 'amplitude' in args
    assert 'bend_rate_angle_ss' in args
    # initialization
    bender = sin_bender(args)
    # paint
    return paint(args, bender)


