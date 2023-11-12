from model import EnergyGrid
import scipy.optimize as optimize

def func_to_optimise(args): # WIND_POWER_MULTIPLIER, INSTALLED_SOLAR_MW, INSTALLED_BATTERY_MW
    a,b,c = args
    grid = EnergyGrid(a,b,c,999999999,NO_TEXT_OUT=True) # INSTALLED_GAS_MW set to functional infinity
    grid = grid
    data = grid.run_model()

    #return data[1] * (1-data[0]) # use inverse percentage to hopefully maximise renewables whilst minimising cost. potentially problematic
    return list(data[:3])  # data[0] is renewable %, data[1]
    """
    if data[0] <=0.98:
        return 9999999999999999999999999
    else:
        return data[1]
    """


wind_res = 4 
solar_res = 4
battery_res = 4

wind_limit = 100 # remember this is a multiplier
solar_limit = 10000
battery_limit = 20000

import csv
with open('Cost_Data.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(["Wind Power Multiplier (MW)", "Installed Solar (MW)", "Installed Battery (MW)", "Renewable Energy (%)", "Cost ($)"])

    for wind_i in range(wind_res):
        for solar_i in range(solar_res):
            for battery_i in range(battery_res):
                wind = wind_i * (wind_limit/wind_res)
                solar = solar_i * (solar_limit/solar_res)
                battery = battery_i * (battery_limit/battery_res)
                writer.writerow([wind,solar,battery] + func_to_optimise([wind,solar,battery]))

print("Data written!")
"""

initial_guess = [2, 6600, 10000]
result = optimize.minimize(func_to_optimise, initial_guess)


if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)
"""




