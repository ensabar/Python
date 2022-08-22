from OwnProjects.motions.motions import linear_constant
from OwnProjects.motions.visualization import plot_function
import visualization
import motions

a = 1
t = range(1,10)

vf = linear_constant(a, t)
plot_function(vf, vf)