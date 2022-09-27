from motions import *
from visualization import *
from reading import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

motion = 'linear'
path = 'OwnProjects\motions\descriptions.json'
plot_type = 'real'

title, x_label, y_label = read_json_plot_properties(path, motion, plot_type)

a = float(input('Acceleration (m/s^2): '))
vi = float(input('Initial velocity (m/s): ' ))
duration = int(input('Time simulation (seg.): '))

dataSet = linear_constant(a, vi, duration)

fig = figure_settings(title, x_label, y_label)

plt.xlim([0,max(dataSet[0]) + 0.1*max(dataSet[0])])
plt.ylim([0,max(dataSet[1]) + 0.1*max(dataSet[1])]) 

run_animation(fig, update, dataSet)
