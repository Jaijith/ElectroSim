import numpy as np
import nonlinear_function as nf

def system_odes(x, t, u, constants):
    # Unpack the state variables, control inputs, and constants
    x1, x2, x3, x4, x5, x6, x7, x8 = x
    u1, u2, u3, u4, u5 = u
    k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18, alpha, beta = constants

    # Define the mass ratio c
    cx2 = x2/(x2 + x3 + x4)
    cx3 = x3/(x2 + x3 + x4)
    print("value for cx2 is: " + str(cx2))
    print("value for cx3 is: " + str(cx3))

    # Define the nonlinear functions g1 to g5
    g1 = nf.g1(cx2, cx3)
    g2 = nf.g2(cx2, x6)
    g3 = nf.g3(cx2, u1)
    g4 = nf.g4(u2)
    g5 = nf.g5(g2, g3, g4, u2)

    # Define the ODEs
    dx1dt = k1*(g1 - x7)/(x1*k0) - k2*(x6 - g1)
    dx2dt = u1 - k3*u2
    dx3dt = u3 - k4*u1
    dx4dt = -(k1*(g1 - x7)/(x1*k0) - k2*(x6 - g1)) + k5*u1
    dx5dt = k6*u2 - u4
    dx6dt = alpha/(x2 + x3 + x4) * (u2*(g5 + u2*u5/(2620*g2)) - k9*(x6 - x7)/(k10 + k11*k0*x1) - (k7*(x6 - g1)**2 - k8*(x6 - g1)*(g1 - x7))/(k0*x1))
    dx7dt = beta/x1 * (-(k12*(x6 - g1)*(g1 - x7) - k13*(g1 - x7)**2)/(k0*x1) + k9*(g1 - x7)/(k15*k0*x1) - k9*(x7 - x8)/(k14 + k15*k0*x1))
    dx8dt = k17*k9*(x7 - x8)/(k14 + k15*k0*x1) - (x8 - k16)/(k14 + k18)

    return [dx1dt, dx2dt, dx3dt, dx4dt, dx5dt, dx6dt, dx7dt, dx8dt]
