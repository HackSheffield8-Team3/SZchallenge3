import matplotlib.pyplot as plt
import numpy as np


# pass this function arrays: hydro data, geo data, solar data
def plot_usage(hydro_data, geo_data, solar_data, wind_data, fossil_data, demand_data):
    n = 17250
    
    
    geo_data = geo_data[:n]
    wind_data = wind_data[:n]
    solar_data = solar_data[:n]
    hydro_data = hydro_data[:n]
    fossil_data = fossil_data[:n]
    demand_data = demand_data[:n]
    
    timeframes = list(range(0, n))
    
    
    
    power_by_type = {
        'geo': geo_data,
        'wind': wind_data,
        'solar': solar_data,
        'hydro': hydro_data,
        'fossil': fossil_data
    }

    fig, ax = plt.subplots()
    ax.stackplot(timeframes, power_by_type.values(),
                 labels=power_by_type.keys(), alpha=0.8)
    ax.plot(timeframes, demand_data)
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Power usage')
    ax.set_xlabel('timestep')
    ax.set_ylabel('Usage (MWh)')

    plt.show()