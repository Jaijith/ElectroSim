# main.py

import numpy as np
from scipy.integrate import odeint
import constants
import equations

# Use the constants, initial conditions, and control functions from constants.py
k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18, alpha, beta = constants.k0, constants.k1, constants.k2, constants.k3, constants.k4, constants.k5, constants.k6, constants.k7, constants.k8, constants.k9, constants.k10, constants.k11, constants.k12, constants.k13, constants.k14, constants.k15, constants.k16, constants.k17, constants.k18, constants.alpha, constants.beta
x1, x2, x3, x4, x5, x6, x7, x8 = constants.x1, constants.x2, constants.x3, constants.x4, constants.x5, constants.x6, constants.x7, constants.x8
u1, u2, u3, u4, u5 = constants.u1, constants.u2, constants.u3, constants.u4, constants.u5

# Define the initial state and control inputs
x0 = [x1, x2, x3, x4, x5, x6, x7, x8]
u = [u1, u2, u3, u4, u5]
constants = [k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18, alpha, beta]

# Time vector
t = np.linspace(0, 10, 100)  # replace with actual time vector

# Solve the system of ODEs
x = odeint(equations.system_odes, x0, t, args=(u, constants))
