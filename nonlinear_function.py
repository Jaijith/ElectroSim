import numpy as np

"""
This module defines the nonlinear functions g1 to g5 for the simulation of the aluminum electrolysis process.
"""

def g1(cx2, cx3):
    """
    Defines the nonlinear function g1, which is related to the heat balance in the system.
    It depends on the mass ratio c and the masses of Al2O3 and ALF3 in the electrolyte.
    It represents the heat generated or absorbed due to the reactions and phase changes in the system.

    Parameters:
    c: The mass ratio.
    x2: The mass of Al2O3 in the electrolyte.
    x3: The mass of ALF3 in the electrolyte.

    Returns:
    The value of g1.
    """
    return 991.2 + 112*cx3 + 61*(cx3**1.5) - 3265.5*(cx3**2.2) - ((793*cx2)/ (-23*cx2*cx3 - (17*(cx3**2)) + 9.36*cx3 + 1))

def g2(cx2, x6):
    """
    Defines the nonlinear function g2, which is related to the reaction kinetics in the system.
    It depends on the mass ratio c, the mass of Al2O3 in the electrolyte, and the temperature of the bath.
    It represents the rate at which the reactions occur in the system.

    Parameters:
    cx2: The mass ratio of Al2O3 in the electrolyte.
    x6: The temperature of the bath.

    Returns:
    The value of g2.
    """
    return np.exp(2.496 - (2068.4/(273 + x6)) - 2.07*cx2)

def g3(cx2, u1):
    """
    Defines the nonlinear function g3, which is related to the control of the system.
    It depends on the mass ratio c, the mass of Al2O3 in the electrolyte, and the control inputs u1, u2, and u3.
    It represents how the control inputs affect the state of the system.

    Parameters:
    cx2: The mass ratio of Al2O3 in the electrolyte.
    u1: The feed rate of Al2O3.
    u2: The current applied to the system.
    u3: The feed rate of ALF3.

    Returns:
    The value of g3.
    """
    x2_crit = 0.01
    return 0.531 + 3.06 * (10**-18) * (u1**3)  - 2.51 * (10**-12) * (u1**2) + 6.96 * (10**-7) * u1 - (14.37*(cx2 - x2_crit) - 0.431) / (735.3*(cx2 - x2_crit) + 1)

def g4(u2):
    """
    Defines the nonlinear function g4, which is related to the electrical properties of the system.
    It depends on the current applied to the system u2.
    It represents how the current affects the electrical properties of the system.

    Parameters:
    u2: The current applied to the system.

    Returns:
    The value of g4.
    """
    return (0.5517 + 3.8168 * (10**-6) * u2) / (1 + 8.271 * (10**-6) * u2)

def g5(g2, g3, g4, u2):
    """
    Defines the nonlinear function g5, which is related to the energy balance in the system.
    It depends on g2, g3, g4, the current applied to the system u2, and the voltage applied to the system u5.
    It represents the energy generated or absorbed due to the electrical inputs and the reactions in the system.

    Parameters:
    g2: The value of g2.
    g3: The value of g3.
    g4: The value of g4.
    u2: The current applied to the system.
    u5: The voltage applied to the system.

    Returns:
    The value of g5.
    """
    return (3.8168 * (10**-6) * g3 * g4 * u2) / (g2 * (1 - g3))
