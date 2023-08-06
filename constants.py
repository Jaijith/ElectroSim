"""
This module defines the constants, initial conditions, and control functions for the simulation of the aluminum electrolysis process.

Constants:
- k0 to k18: These are constants used in the equations that describe the system dynamics. They represent various physical properties and parameters of the system, such as reaction rates, heat transfer coefficients, and electrical properties.
- alpha, beta: These are constants used in the equations that describe the system dynamics. They represent heat transfer coefficients.

Initial conditions for system variables:
- x1: Initial mass of the side ledge.
- x2: Initial mass of Al2O3 in the electrolyte.
- x3: Initial mass of ALF3 in the electrolyte.
- x4: Initial mass of Na3AlF6 in the electrolyte.
- x5: Initial mass of metal.
- x6: Initial temperature of the bath.
- x7: Initial temperature of the side ledge.
- x8: Initial temperature of the wall.
- x2_cirt :  critical value for the mass ratio of Al2O3 (x2) in the electrolyte.

Control functions:
- u1: Feed rate of Al2O3.
- u2: Current applied to the system.
- u3: Feed rate of ALF3.
- u4: Rate of metal tapping.
- u5: Voltage applied to the system.
"""
import numpy as np
# Constants
k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18 = 2e-5, 7.5e-4, 0.18, 1.7e-7, 0.036, 0.03, 4.43e-8, 338, 1.41, 17.92, 0.00083, 0.2, 237.5, 0.99, 0.0077, 0.2, 35, 5.8e-7,0.04  # replace with actual values
alpha, beta = 5.66e-4, 7.58e-4  # replace with actual values

x1 = np.random.uniform(3260, 3260)  # replace with actual initial conditions
x2 = np.random.uniform(700, 1400) # production rate is 100kg per hour, implies 193 kg of consumption per hour (6 hour shift)
x3 = np.random.uniform(3500, 7000)
cx2 = np.random.uniform(0.02, 0.03)
cx3 = np.random.uniform(0.10, 0.11)
x4 = np.random.uniform(13500, 14000)
x5 = np.random.uniform(9950, 10000)
x6 = np.random.uniform(975, 975)
x7 = np.random.uniform(816, 816)
x8 = np.random.uniform(580, 580)

'''# Control functions
u1 = np.random.uniform(3e4 * (0.023 - x2), 3e4 * (0.023 - x2))  # replace with actual control inputs
u2 = np.random.uniform(14e3, 14e3)
u3 = np.random.uniform(13e3 * (0.105 - x3), 13e3 * (0.105 - x3))
u4 = np.random.uniform(2 * (x5 - 10e3), 2 * (x5 - 10e3))
u5 = np.random.uniform(0.05, 0.05)'''


import numpy as np

# Constants
# ... (same as before)

# Deterministic part of the control functions
def u1_deterministic(cx2):
    return 3e4 * (0.023 - cx2)

def u2_deterministic():
    return 14e3

def u3_deterministic(cx3):
    return 13e3 * (0.105 - cx3)

def u4_deterministic(x5):
    return 2 * (x5 - 10e3)

def u5_deterministic():
    return 0.05

# Function to generate the random term for the control functions
def random_term(interval):
    return np.random.uniform(interval[0], interval[1])
