# animated_line_plot.py

from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def figure_settings(title, x_label, y_label):
    fig, ax = plt.subplots()
    
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


# function that draws each frame of the animation
def update(num, dataSet, ax):
    # create the figure and axes objects
    ax.clear()
    ax.plot(dataSet[0, :num], dataSet[1, :num])
    
    ax.set_xlim([0,max(dataSet[0]) + 0.1*max(dataSet[0])])
    ax.set_ylim([0,max(dataSet[1]) + 0.1*max(dataSet[1])])

# run the animation
def run_animation(fig, animate):
    ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)
    plt.show()