# animated_line_plot.py

from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



# create the figure and axes objects
fig, ax = plt.subplots()


# function that draws each frame of the animation
def update(num, dataSet):


    ax.clear()
    ax.plot(dataSet[:num], dataSet[:num])
    ax.set_xlim([0,20])
    ax.set_ylim([0,10])
    

# run the animation
def run_animation(fig, animate):
    ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)
    plt.show()