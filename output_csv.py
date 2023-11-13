from model import EnergyGrid
import scipy.optimize as optimize
import csv

def func_to_optimise(args): # WIND_POWER_MULTIPLIER, INSTALLED_SOLAR_MW, INSTALLED_BATTERY_MW
    a,b,c = args
    grid = EnergyGrid(a,b,c,1e10,NO_TEXT_OUT=True) # INSTALLED_GAS_MW set to functional infinity
    grid = grid
    data = grid.run_model()

    #return data[1] * (1-data[0]) # use inverse percentage to hopefully maximise renewables whilst minimising cost. potentially problematic
    return [data[0], data[1]/data[2]]  # data[0] is renewable %, data[1] is cost ($), total usage (MWh) 
    """
    if data[0] <=0.98:
        return 9999999999999999999999999
    else:
        return data[1]
    """

res = 3 # note that no. of lines is (res+1)^n and this will affect runtime, thought they can be set individually

wind_res = res
solar_res = res
battery_res = res

wind_min = 4.45
solar_min = 84e3
battery_min = 0

wind_limit = 4.5 #1e3 # remember this is a multiplier
solar_limit = 85e3 #1e6
battery_limit = 1e3 #5e5

mode = "a"
#from tqdm import tqdm

with open("Cost_Data_Aggregate.csv", mode, newline='') as f:
    writer = csv.writer(f)
    if mode == "w":
        writer.writerow(["Wind Power Multiplier (MW)", "Installed Solar (MW)", "Installed Battery (MW)", "Renewable Energy (%)", "Cost ($/MWh)"])

    for wind_i in range(wind_res+1): #next: add trange or tqdm wrapper for nested progress bars
        for solar_i in range(solar_res+1):
            for battery_i in range(battery_res+1):
                wind = wind_min + (wind_i * (wind_limit - wind_min)/wind_res)
                solar = solar_min + (solar_i * (solar_limit - solar_min)/solar_res)
                battery = battery_min + (battery_i * (battery_limit - battery_min)/battery_res)
                writer.writerow([wind,solar,battery] + func_to_optimise([wind,solar,battery]))

"""

initial_guess = [2, 6600, 10000]
result = optimize.minimize(func_to_optimise, initial_guess)


if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)
"""




