import matplotlib.pyplot as plt
import numpy as np


# pass this function arrays: hydro data, geo data, solar data
def plot_usage(hydro_data, geo_data, solar_data, wind_data, fossil_data, demand_data):
    
    geo_data = geo_data[:200]
    wind_data = wind_data[:200]
    solar_data = solar_data[:200]
    hydro_data = hydro_data[:200]
    fossil_data = fossil_data[:200]
    demand_data = demand_data[:200]
    
    
    
    
    timeframes = list(range(0, 200))
    
    
    
    power_by_type = {
        'geo': geo_data,
        'wind': wind_data,
        'solar': solar_data,
        'hydro': hydro_data
    }

    fig, ax = plt.subplots()
    ax.stackplot(timeframes, power_by_type.values(),
                 labels=power_by_type.keys(), alpha=0.8)
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Power usage')
    ax.set_xlabel('timestep')
    ax.set_ylabel('Usage (MWh)')

    plt.show()