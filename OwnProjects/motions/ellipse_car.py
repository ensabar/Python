import numpy as np
import matplotlib.pyplot as plt
# a > b
a = 1.2 # semi-major axis
b = 1   # semi-minor axis

e = np.sqrt(1 - b**2 / a**2) # eccentricity

theta = np.linspace(0, 2 * np.pi, 100)

r_x = a * np.cos(theta)
r_y = b * np.sin(theta)

plt.plot(r_x, r_y)
plt.show()