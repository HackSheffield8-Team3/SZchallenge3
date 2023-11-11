import pandas, hydro_model

class EnergyGrid():
    def __init__(self, WIND_POWER_MULTIPLIER, INSTALLED_SOLAR_MW):
        with open("historic_demand_points.txt", "r") as dp_file:
            self.DEMAND_POINTS_STRINGS = dp_file.readlines()

        self.DEMAND_POINTS = [int(x) for x in self.DEMAND_POINTS_STRINGS]
        
        self.NUMBER_OF_TIME_STEPS = len(self.DEMAND_POINTS)

        # Solar data is based on 64.8MW installed
        SOLAR_POWER_MULTIPLIER = INSTALLED_SOLAR_MW/64.8

        self.generation_data = pandas.DataFrame({
            "geo": self.geo_array(),
            "wind": self.wind_array(WIND_POWER_MULTIPLIER),
            "solar": self.solar_array(SOLAR_POWER_MULTIPLIER)
        })

        self.hydro_model = hydro_model.HydroModel(10000, 1000, 10000)


    def geo_array(self):
        with open("historic_geo_generation.txt") as hgg_file:
            hgg_array = hgg_file.readlines()
        return [int(x) for x in hgg_array]

    def wind_array(self, WIND_POWER_MULTIPLIER):
        with open("historic_wind_generation.txt") as hwg_file:
            hwg_array = hwg_file.readlines()

        return [int(hwg_array[i])*WIND_POWER_MULTIPLIER for i in range(self.NUMBER_OF_TIME_STEPS)]
    
    def solar_array(self, SOLAR_POWER_MULTIPLIER):
        with open("historic_solar_generation.txt") as hsg_file:
                hsg_array = hsg_file.readlines()
        
        return [int(hsg_array[i])*SOLAR_POWER_MULTIPLIER for i in range(self.NUMBER_OF_TIME_STEPS)]




    
    def model_time_step(self, time):
        print(f"Time {time}\nDemand is {self.DEMAND_POINTS[time]}")
        total_demand = self.DEMAND_POINTS[time]
        remaining_demand = total_demand

        # Subtracting the dc1
        dc1 =  self.generation_data.iloc[time]["geo"]
        print(f"dc1: {dc1}")
        remaining_demand = remaining_demand - dc1

        # Calculating the amount of dc2
        dc2 = min(self.generation_data.iloc[time]["wind"] + self.generation_data.iloc[time]["solar"], remaining_demand)
        print(f"dc2: {dc2}")

        print("\n")

    def run_model(self):
        for current_time in range(self.NUMBER_OF_TIME_STEPS):
            self.model_time_step(current_time)
        print("Model done")