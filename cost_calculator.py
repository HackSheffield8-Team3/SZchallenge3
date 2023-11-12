def calculate_cost(hydro, geo, coal, gas, wind, solar, other, battery_MWh):
    hydro_cost = hydro * 50
    geo_cost = geo * 70
    coal_cost = coal * 200
    gas_cost = gas * 100
    wind_cost = wind * 60
    solar_cost = solar * 40
    other_cost = other * 150
    battery_cost = battery_MWh * 500
        
    return hydro_cost + geo_cost + coal_cost + gas_cost + wind_cost + solar_cost + other_cost + battery_cost
        