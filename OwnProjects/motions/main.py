from motions import *
from visualization import *
from reading import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
motion = input('Kind of motion to visualize?: ').lower()
path = 'OwnProjects\motions\descriptions.json'

if (motion == 'linear'):
    title, x_label, y_label = read_json_plot_properties(path, 'linear')

    a = float(input('Acceleration (m/s^2): '))
    vi = float(input('Initial velocity (m/s): ' ))
    duration = int(input('Time simulation (seg.): '))
    dataSet = linear_constant(a, vi, duration)
    fig = figure_settings(title, x_label, y_label)
    run_animation(fig, update, dataSet)
elif (motion == 'accelerated'):  
    plot_type = input ('Which kind of visualization you want? [real/phase]:  ')
    if (plot_type == 'real'):
        pass
    
    elif (plot_type == 'phase'):
        pass

