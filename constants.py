import numpy as np

# Constants
k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18 = 2e-5, 7.5e-4, 0.18, 1.7e-7, 0.036, 0.03, 4.43e-8, 338, 1.41, 17.92, 0.00083, 0.2, 237.5, 0.99, 0.0077, 0.2, 35, 5.8e-7,0.04
alpha, beta = 5.66e-4, 7.58e-4

x1 = np.random.uniform(3260, 3260)
x2 = np.random.uniform(700, 1400)
x3 = np.random.uniform(3500, 7000)
cx2 = np.random.uniform(0.02, 0.03)
cx3 = np.random.uniform(0.10, 0.11)
x4 = np.random.uniform(13500, 14000)
x5 = np.random.uniform(9950, 10000)
x6 = np.random.uniform(975, 975)
x7 = np.random.uniform(816, 816)
x8 = np.random.uniform(580, 580)

# Control functions
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
