import numpy as np
import matplotlib.pyplot as plt

R = 10 # radius of orbit
theta = np.linspace(0,2*np.pi, 100)
# Using vectors 
r_x = R * np.cos(theta)
r_y = R * np.sin(theta)

plt.plot(r_x, r_y)
plt.show()
#theta_x = R * np.cos(theta + np.pi/2)
#theta_y = R * np.sin(theta + np.pi/2)

#u_r = (r_x / np.linalg.norm(r_x), r_y / np.linalg.norm(r_y))
#u_theta = (theta_x / np.linalg.norm(theta_x), theta_y / np.linalg.norm(theta_y)) # not sure if its best way to obtain orthogonal vector

#print(np.linalg.multi_dot([u_r[1], u_theta[1]])) # to check if they are orthogonal
