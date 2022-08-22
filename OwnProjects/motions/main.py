from motions import *
from visualization import *
from matplotlib.animation import FuncAnimation

a = 1
duration = 100
vi = 0
type = input('Kind of motion to visualize?: ')
type.lower()

if (type == 'linear'):
    a = float(input('Acceleration (m/s^2): '))
    vi = float(input('Initial velocity (m/s): ' ))
    duration = int(input('Time simulation (seg.): '))
    #
    dataSet = linear_constant(a, vi, duration)
    

# create empty lists for the x and y data


ani = FuncAnimation(fig, update, frames= 500,  fargs=[dataSet])
plt.show()