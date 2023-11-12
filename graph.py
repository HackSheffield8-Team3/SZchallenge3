import matplotlib.pyplot as plt
import numpy as np


# pass this function arrays: hydro data, geo data, solar data
def plot_usage(hydro_data, geo_data, solar_data):
    
    n=100
    
    timeframes = list(range(0, len(hydro_data)))
    
    power_by_type = {
        'hydro': hydro_data[:n],
        'geo': geo_data[:n],
        'solar': solar_data[:n],
    }

    fig, ax = plt.subplots()
    ax.stackplot(timeframes, power_by_type.values(),
                 labels=power_by_type.keys(), alpha=0.8)
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Power usage')
    ax.set_xlabel('timestep')
    ax.set_ylabel('Usage (MWh)')

    plt.show()