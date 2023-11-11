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

    
    def consume_energy(self, source, amount=None):
        """
        Records the consumption of a specific quantity of energy and updates the remaining energy accordingly. If amount is None, as much is consumed as is available up to the remaining amount
        """
        if amount is None:
            amount = min(self.current_timestep_remaining_demand, self.available_generation_data[source][self.current_timestep])
        
        self.current_timestep_remaining_demand -= amount
        self.usage_data[source] += amount
        print(f"  - {source}: {round(amount,2)}")


    
    def model_time_step(self):
        self.current_timestep_total_demand = self.DEMAND_POINTS[self.current_timestep]
        self.current_timestep_remaining_demand = self.DEMAND_POINTS[self.current_timestep]
        print(f"Timestep {self.current_timestep}\nDemand: {self.current_timestep_total_demand}")

        # dc1
        print("dc1")
        self.consume_energy("hydro", amount=self.hydro_model.hydro_model_DC1(self.current_timestep_remaining_demand))
        self.consume_energy("geo")

        # Subtracting the dc2 - use solar then wind as solar is cheaper
        print("dc2")
        self.consume_energy("solar")
        self.consume_energy("wind")

        # Subtracting the dc3
        dc3 = min(0, remaining_demand)
        print(f"dc3: {round(dc3,2)}")

        # Subtracting the dc4
        dc4 = min(0, remaining_demand)
        print(f"dc4: {round(dc4,2)}")

        if self.current_timestep_remaining_demand==0:
            print("\033[92mDemand met!\033[0m")
        elif self.current_timestep_remaining_demand>0:
            print("\033[91mDemand not met!\033[0m")
        else:
            print("\033[91mGeneration exceeded demand!\033[0m")


        print("\n")

    def run_model(self):
        for self.current_timestep in range(self.NUMBER_OF_TIME_STEPS):
            self.model_time_step()
        print("Model done")