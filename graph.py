import matplotlib.pyplot as plt

# pass this function an array of hydro_usage every time step, in MW.
def plot_usage(hydro_data):
    plt.plot(hydro_data)
    plt.ylabel('hydro usage')
    plt.show()