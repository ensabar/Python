import numpy as np
import matplotlib.pyplot as plt




k = 1.8 # N/m
m = 3 # g

rads = np.arange(0, 2*np.pi, 0.01)
T = 2*np.pi*np.sqrt(m/k)
w = 2*np.pi/T
c1 = np.float16(0) # initial position to zero
c2 = np.float16(5)*w # initial velocity
t = np.linspace(0, 20, len(rads))
xi = []
x = []
vi = []
v = []

phi = np.divide(c2, c1, out=np.zeros_like(c2), where=c1!=0) # to avoid 0/0
A = np.abs(c1 + c2*1j)

for rad in range(len(rads)):

    
    x.append(A*np.sin(w*t[rad] + phi))

    #c1 = x[rad]
    v.append(-A*w * np.sin(w*t[rad] - phi))

    #c2 = v[rad]
    
plt.polar(v, x)
plt.show()
#v = np.array(v)
#dataSet = np.array([rads, x])