import matplotlib.pyplot as plt


def plot_usage(hydro_data):
    plt.plot(hydro_data)
    plt.ylabel('hydro usage')
    plt.show()