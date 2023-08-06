import matplotlib.pyplot as plt
import numpy as np

def plot_simulation_results(t, x, u, delta_t_rand):
    # Create a new figure
    fig = plt.figure(figsize=(10, 20))

    # Define the names of the state variables
    state_names = ['Mass of side ledge', 'Mass of Al2O3', 'Mass of ALF3', 'Mass of Na3AlF6', 'Mass of metal', 'Temperature of bath', 'Temperature of side ledge', 'Temperature of wall']

    # Plot the state variables
    for i in range(x.shape[1]):
        ax = fig.add_subplot(x.shape[1] + u.shape[1], 1, i+1)
        ax.plot(t, x[:, i])
        ax.set_ylabel(state_names[i])
        for j in np.arange(0, t[-1], delta_t_rand):
            ax.axvline(x=j, color='r', linestyle='--')

    # Define the names of the control inputs
    control_names = ['Feed rate of Al2O3', 'Current', 'Feed rate of ALF3', 'Rate of metal tapping', 'Voltage']

    # Plot the control inputs
    for i in range(u.shape[1]):
        ax = fig.add_subplot(x.shape[1] + u.shape[1], 1, x.shape[1] + i+1)
        ax.plot(t, u[:, i])
        ax.set_ylabel(control_names[i])
        for j in np.arange(0, t[-1], delta_t_rand):
            ax.axvline(x=j, color='r', linestyle='--')

    # Set the x-label for the last subplot
    ax.set_xlabel('Time')

    # Show the figure
    plt.tight_layout()
    plt.show()
