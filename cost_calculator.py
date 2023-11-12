"""
class documentation
"""
class CostCalculator ():

    def calculate_cost(hydro_DC1, geo, coal, wind, solar,  hydro_DC3, other, battery_MWh):
        hydro = hydro_DC1 + hydro_DC3
        hydro_cost = (hydro/2) * 50
        geo_cost = (geo/2) * 70
        