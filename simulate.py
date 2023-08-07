import numpy as np
from scipy.integrate import odeint
import constants
import equations

def denormalize_action(action):
    u1_min, u1_max = 0, 3e4 * (0.023 - constants.cx2)
    u2_min, u2_max = 0, 14e3
    u3_min, u3_max = 0, 13e3 * (0.105 - constants.cx3)
    u4_min, u4_max = 0, 2 * (constants.x5 - 10e3)
    u5_min, u5_max = 0, 0.05

    u1 = action[0] * (u1_max - u1_min) + u1_min
    u2 = action[1] * (u2_max - u2_min) + u2_min
    u3 = action[2] * (u3_max - u3_min) + u3_min
    u4 = action[3] * (u4_max - u4_min) + u4_min
    u5 = action[4] * (u5_max - u5_min) + u5_min

    return [u1, u2, u3, u4, u5]

def simulate(time, action, alumina_interval, alumina_amount):
    u = denormalize_action(action)
    x0 = [constants.x1, constants.x2, constants.x3, constants.x4, constants.x5, constants.x6, constants.x7, constants.x8]
    constants_values = [constants.k0, constants.k1, constants.k2, constants.k3, constants.k4, constants.k5, constants.k6, constants.k7, constants.k8, constants.k9, constants.k10, constants.k11, constants.k12, constants.k13, constants.k14, constants.k15, constants.k16, constants.k17, constants.k18, constants.alpha, constants.beta]

    t = np.linspace(0, time, alumina_interval)
    x = np.zeros((len(t), len(x0)))
    x[0, :] = x0

    for i in range(len(t)-1):
        if i % (alumina_interval*10) == 0:
            u[0] += alumina_amount
        x_step = odeint(equations.system_odes, x0, [t[i], t[i+1]], args=(u, constants_values))
        x[i+1, :] = x_step[-1, :]
        x0 = x_step[-1, :]

    return t, x
