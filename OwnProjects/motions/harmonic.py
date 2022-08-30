import numpy as np
import matplotlib.pyplot as plt
'''
phi determina la posicion inicial, como se utiliza coseno pues para que empieze en t= 0 y x=0 se necesita phi = pi/2
'''
k = 1.8 # N/m
m = 3 # g
phi = np.pi/2

rads = np.arange(0, 2*np.pi, 0.01)
T = 2*np.pi*np.sqrt(m/k)
w = 2*np.pi/T
c1 = np.float16(0) # initial position to zero
c2 = np.float16(1)*w # initial velocity
t = np.linspace(0, 10, len(rads))

x = []
v = []
a = []

A = np.abs(c1 + c2*1j)

for rad in range(len(rads)):
    # p = 2*A * np.sin(w*t[rad])
    x.append( A * np.cos(w*t[rad] - phi)) # x(t)
    v.append(-A*w * np.sin(w*t[rad] - phi)) # v(t)
    a.append(-A*w**2 * np.cos(w*t[rad] - phi)) # a(t)

plt.plot(t, x, t, v, t, a)

plt.title('SHM')
#plt.xlabel('time')
#plt.ylabel('Position')
plt.show()
#v = np.array(v)
#dataSet = np.array([rads, x])