import numpy as np
import matplotlib.pyplot as plt

# Definition of different types of motion


def simple_harmonic(a, b):

    return a + b

def linear_constant(a, vi, duration):
    t = np.linspace(1,duration, duration)
    vf = vi + a*t
    dataSet = np.array([t, vf])
    return dataSet