import numpy as np
import matplotlib.pyplot as plt

R = 10 # radius of orbit
theta = np.linspace(0,2*np.pi, 100)
R = [10] * len(theta)

plt.polar(theta, R)
plt.show()
