import numpy as np
import matplotlib.pyplot as plt




k = 1.8 # N/m
m = 3 # g   


t = np.linspace(1,2*np.pi,50)
T = 2*np.pi*np.sqrt(m/k)
w = 2*np.pi/T
c1 = np.float16(0) # initial position to zero
c2 = np.float16(5)*w # initial velocity

xi = []
x = []
vi = []
v = []
for i in range(len(t)):
    phi = np.divide(c2, c1, out=np.zeros_like(c2), where=c1!=0)
    A = np.abs(c1 + c2*1j)
    xi = A*np.cos(w*t[i] - phi)
    x.append(xi)
    c1 = np.float16(xi)
    vi= -A*w * np.sin(w*t[i] - phi)
    v.append(vi)
    c2 = np.float16(vi)
v = np.array(v)
dataSet = np.array([t, x])