from motions import *
from visualization import *
from reading import *
from matplotlib.animation import FuncAnimation
from matplotlib import animation

type = input('Kind of motion to visualize?: ').lower()
path = 'OwnProjects\motions\descriptions.json'

if (type == 'linear'):
    title, x_label, y_label = read_json_plot_properties(path, 'linear')

    a = float(input('Acceleration (m/s^2): '))
    vi = float(input('Initial velocity (m/s): ' ))
    duration = int(input('Time simulation (seg.): '))
    dataSet = linear_constant(a, vi, duration)
    
    fig, ax = figure_settings(title, x_label, y_label)



ani = animation.FuncAnimation(fig, update,  fargs=[dataSet], interval = 100)
plt.show()