# main.py

import numpy as np
from scipy.integrate import odeint
import constants
import equations
import plotting# main.py

import numpy as np
from scipy.integrate import odeint
import constants
import equations
import plotting

# Define the initial state and control inputs
x0 = [constants.x1, constants.x2, constants.x3, constants.x4, constants.x5, constants.x6, constants.x7, constants.x8]
constants_values = [constants.k0, constants.k1, constants.k2, constants.k3, constants.k4, constants.k5, constants.k6, constants.k7, constants.k8, constants.k9, constants.k10, constants.k11, constants.k12, constants.k13, constants.k14, constants.k15, constants.k16, constants.k17, constants.k18, constants.alpha, constants.beta]

# Time vector
t = np.linspace(0, 1000*30, 1000)  # replace with actual time vector

# Interval for the random term of the control functions
random_term_interval_u1 = [-2.0, 2.0]  # replace with actual interval
random_term_interval_u2 = [-7e3, 7e3] 
random_term_interval_u3 = [-0.5, 0.5]
random_term_interval_u4 = [-2.0, 2.0] 
random_term_interval_u5 = [-0.015, 0.015]

# Time step for changing the random term
delta_t_rand = 30*30  # ∆Trand = 30∆T

# Initialize the control functions
u = [constants.u1_deterministic(x0[1]) + constants.random_term(random_term_interval_u1),
     constants.u2_deterministic() + constants.random_term(random_term_interval_u2),
     constants.u3_deterministic(x0[2]) + constants.random_term(random_term_interval_u3),
     constants.u4_deterministic(x0[4]) + constants.random_term(random_term_interval_u4),
     constants.u5_deterministic() + constants.random_term(random_term_interval_u5)]

# Initialize the time for the next change of the random term
t_rand_next = delta_t_rand

# Solve the system of ODEs
x = []
u_plot = []
for i in range(len(t) - 1):
    # Solve the system of ODEs for the current time step
    x_i = odeint(equations.system_odes, x0, [t[i], t[i+1]], args=(u, constants_values))
    x.append(x_i[0])
    
    # Update the initial state for the next time step
    x0 = x_i[-1]

    # Store the control inputs for the current time step
    u_plot.append(u)
    
    # If it's time to change the random term, update the control functions
    if t[i+1] >= t_rand_next:
        u = [constants.u1_deterministic(x0[1]) + constants.random_term(random_term_interval_u1),
             constants.u2_deterministic() + constants.random_term(random_term_interval_u2),
             constants.u3_deterministic(x0[2]) + constants.random_term(random_term_interval_u3),
             constants.u4_deterministic(x0[4]) + constants.random_term(random_term_interval_u4),
             constants.u5_deterministic() + constants.random_term(random_term_interval_u5)]
        t_rand_next += delta_t_rand

# Convert the list of state vectors to a 2D array
x = np.array(x)
u_plot = np.array(u_plot)

# Plot the results
plotting.plot_simulation_results(t[:-1], x, u_plot, delta_t_rand)