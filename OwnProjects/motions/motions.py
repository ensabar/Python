import numpy as np
import matplotlib.pyplot as plt

# Definition of different types of motion


#def simple_harmonic(m, k):
    # x = A*cos(wt - phi)
    # v = -A*w * sin(wt - phi)
    # A = |c1 + i*c2|
    # phi = arctg(c2/c1)
    # In the solution, c1 and c2 are two constants determined by the initial conditions 
    # (specifically, the initial position at time t = 0 is c1, while the initial velocity is c2*ω),
    # and the origin is set to be the equilibrium position.
    # w = 2*pi*f
    # f = 1 / T
    # T = 2*pi*sqrt(m/k)
k = 1.8 # N/m
m = 3 # m
c1 = np.float16(0) # initial position to zero
c2 = np.float16(0) # initial velocity
t = np.linspace(1,20,20)
T = 2*np.pi*np.sqrt(m/k)
w = 2*np.pi/T

xi = []
x = []
vi = []
v = []

for i in range(len(t)):
    try:
        phi = np.arctan(c2/c1)
    except ZeroDivisionError:
        phi = 0
    
    A = np.abs(c1 + c2*1j)

    xi = A*np.cos(w*t[i] - phi)
    x.append(xi)
    c1 = np.int_(xi)
    vi= -A*w * np.sin(w*t[i] - phi)
    v.append(vi)
    c2 = np.int_(vi)
    #return a + b

def linear_constant(a, vi, duration):
    t = np.linspace(1,duration, duration)
    vf = vi + a*t
    dataSet = np.array([t, vf])
    return dataSet

#def linear_accelerated()