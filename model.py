import hydro_model

class EnergyGrid():
    def __init__(self, WIND_POWER_MULTIPLIER, INSTALLED_SOLAR_MW):
        with open("historic_demand_points.txt", "r") as dp_file:
            self.DEMAND_POINTS_STRINGS = dp_file.readlines()

        self.DEMAND_POINTS = [int(x) for x in self.DEMAND_POINTS_STRINGS]
        
        self.NUMBER_OF_TIME_STEPS = len(self.DEMAND_POINTS)

        # Solar data is based on 64.8MW installed
        SOLAR_POWER_MULTIPLIER = INSTALLED_SOLAR_MW/64.8

        self.available_generation_data = {
            "geo": self.geo_array(),
            "wind": self.wind_array(WIND_POWER_MULTIPLIER),
            "solar": self.solar_array(SOLAR_POWER_MULTIPLIER)
        }

        self.usage_data = {
            "geo": 0,
            "wind": 0,
            "solar": 0,
            "hydro": 0
        }

        self.generation_data = {
            "geo": 0,
            "wind": 0,
            "solar": 0,
            "hydro": 0
        }

        self.hydro_model = hydro_model.HydroModel(10000, 1000, 10000)

        self.total_wind_used = 0


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
        print(f"Timestep {time}\nDemand: {self.DEMAND_POINTS[time]}")
        total_demand = self.DEMAND_POINTS[time]
        remaining_demand = total_demand

        # Subtracting the dc1
        remaining_demand -= self.hydro_model.hydro_model_DC1(remaining_demand)
        self.used_generation_data["hydro"] += self.hydro_model.hydro_model_DC1(remaining_demand)
        print(f"dc1-hydro: {self.hydro_model.hydro_model_DC1(remaining_demand)}")

        # Subtracting the dc2 - use solar then wind as solar is cheaper
        dc2_solar = min(self.generation_data["solar"][time], remaining_demand)
        remaining_demand -= dc2_solar
        self.used_generation_data["solar"] += dc2_solar
        print(f"dc2-solar: {dc2_solar}")

        dc2_wind = min(self.generation_data["wind"][time], remaining_demand)
        remaining_demand -= dc2_wind
        self.used_generation_data["solar"] += dc2_wind
        print(f"dc2-wind: {dc2_wind}")

        # Subtracting the dc3
        dc3 = min(0, remaining_demand)
        print(f"dc3: {dc3}")
        remaining_demand = remaining_demand - dc3

        # Subtracting the dc4
        dc4 = min(0, remaining_demand)
        print(f"dc4: {dc4}")
        remaining_demand = remaining_demand - dc4

        if remaining_demand==0:
            print("\033[92mDemand met!\033[0m")
        elif remaining_demand>0:
            print("\033[91mDemand not met!\033[0m")
        else:
            print("\033[91mGeneration exceeded demand!\033[0m")


        print("\n")

    def run_model(self):
        for current_time in range(self.NUMBER_OF_TIME_STEPS):
            self.model_time_step(current_time)
        print("Model done")