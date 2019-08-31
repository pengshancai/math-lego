from lego_basic import paint_const, paint_sin, paint_linear

delta = 0.0
line_width1 =9
line_width2 = 6
line_width3 = 1.5

def paint_sunshine(args):
    assert 'x' in args
    assert 'angle' in args
    assert 'color' in args
    # Part 1
    args = {
        'x': args['x'],
        'angle': args['angle'] - 8,
        'color': args['color'],
        'num_steps': 32,
        'bend_rate': -0.5,
        'step_size': 0.003,
        'line_width': (line_width1, line_width2),
        'delta': delta
    }
    x, angle, bend_rate = paint_const(args)
    # Part 2
    args = {
        'x': x,
        'angle': angle,
        'color': args['color'],
        'num_steps': 100,
        'init_bend_rate': bend_rate,
        'target_bend_rate': 10,
        'step_size': 0.003,
        'line_width': (line_width2, line_width3),
        'delta': delta
    }
    x, angle, bend_rate = paint_linear(args)
    return x, angle, bend_rate