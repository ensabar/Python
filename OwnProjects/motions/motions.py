import numpy as np
import matplotlib.pyplot as plt

# Definition of different types of motion


def simple_harmonic(a, b):

    return a + b

def linear_constant(a, vi, duration):
    duration = np.linspace(1,duration, 100)

    vf = vi + a*duration
    dataSet = np.array([duration, vf])
    return dataSet