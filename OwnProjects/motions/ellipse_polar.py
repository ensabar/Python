import numpy as np
import matplotlib.pyplot as plt
# a > b
a = 1.8 # semi-major axis
b = 1   # semi-minor axis

e = np.sqrt(1 - b**2 / a**2) # eccentricity

theta = np.linspace(0, 2 * np.pi, 100)
# polar form relative to center
r_center = b / np.sqrt(1 - (e*np.cos(theta))**2)

# polar form relative to focus
phi = 0 # angular coordinate of the other focus
r_focus = (a * (1 - e**2)) / (1 - e*np.cos(theta - phi))

plt.polar(theta, r_focus)

plt.show()