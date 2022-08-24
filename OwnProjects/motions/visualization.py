from random import randint
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation

def figure_settings(title, x_label, y_label):
    fig= plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return fig


# function that draws each frame of the animation
def update(num, dataSet):
    
    # create the figure and axes objects
    #plt.clf() # if i clean every iteration axes are broken
    plt.plot(dataSet[0, :num], dataSet[1, :num], c = 'blue')
    
    
# run the animation
def run_animation(fig, animate, dataSet):
    ani = animation.FuncAnimation(fig, update,  fargs=[dataSet], interval = 200, repeat_delay = 1000)
    plt.show()