import matplotlib.pyplot as plt
import numpy as np


# pass this function an array of hydro_usage every time step, in MW.
def plot_usage(timesteps, hydro_data, geo_data, solar_data):
    timeframes = timeframes
    power_by_type = {
        'hydro': hydro_data,
        'geo': geo_data,
        'solar': solar_data,
    }

    fig, ax = plt.subplots()
    ax.stackplot(timeframes, power_by_type.values(),
                 labels=power_by_type.keys(), alpha=0.8)
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Power usage')
    ax.set_xlabel('timestep')
    ax.set_ylabel('Usage (MW30m)')

    plt.show()