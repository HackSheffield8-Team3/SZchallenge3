import hydro_model, wind_model, battery_model, tabulate, graph

class EnergyGrid():
    def __init__(self, WIND_POWER_MULTIPLIER, INSTALLED_SOLAR_MW, INSTALLED_BATTERY_MW):
        with open("historic_demand_points.txt", "r") as dp_file:
            self.DEMAND_POINTS_STRINGS = dp_file.readlines()

        self.DEMAND_POINTS = [int(x) for x in self.DEMAND_POINTS_STRINGS]
        
        self.NUMBER_OF_TIME_STEPS = len(self.DEMAND_POINTS)

        self.INSTALLED_BATTERY_MW = INSTALLED_BATTERY_MW

        # Solar data is based on 64.8MW installed
        SOLAR_POWER_MULTIPLIER = INSTALLED_SOLAR_MW/64.8

        self.available_generation_data = {
            "geo": self.geo_array(),
            "wind": self.wind_array(WIND_POWER_MULTIPLIER),
            "solar": self.solar_array(SOLAR_POWER_MULTIPLIER)
        }

        self.usage_data_totals = {
            "geo": 0,
            "wind": 0,
            "solar": 0,
            "hydro": 0,
            "fossil": 0
        }

        self.generation_totals = {
            "geo": 0,
            "wind": 0,
            "solar": 0,
            "hydro": 0,
            "fossil": 0
        }

        self.usage_data_arrays = {
            "geo": [],
            "wind": [],
            "solar": [],
            "hydro": [],
            "fossil": []
        }


        self.generation_arrays = {
            "geo": [],
            "wind": [],
            "solar": [],
            "hydro": [],
            "fossil": []
        }

        self.gen_status_counts = {
            "match": 0,
            "excess": 0,
            "deficit": 0
        }

        self.hydro_model = hydro_model.HydroModel(10000, 1000, 10000)
        self.wind_model = wind_model.WindModel()
        self.battery = battery_model.BatteryModel(INSTALLED_BATTERY_MW, 0)

    def add_to_usage_data(self, source, mwhalfhours):
        self.usage_data_totals[source] += mwhalfhours/2
        self.usage_data_arrays[source].append(mwhalfhours/2)

    def add_to_generation_data(self, source, mwhalfhours):
        self.generation_totals[source] += mwhalfhours/2
        self.generation_arrays[source].append(mwhalfhours/2)


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
        Records the consumption of a specific quantity of energy and updates the remaining energy accordingly.
        If amount is None, as much is consumed as is available up to the remaining amount
        Returns the amount consumed
        """
        amount = min(self.current_timestep_remaining_demand, self.available_generation_data[source][self.current_timestep])
        
        self.current_timestep_remaining_demand -= amount
        self.add_to_usage_data(source, amount)
        self.add_to_generation_data(source, amount)
        print(f"  - {source}: {round(amount,2)}")
        return amount

    def summary_statistics(self):
        print("\033[1mSummary statistics\033[0m")

        headers = [
          "Source", "Generated (GWh)", "Used (GWh)", "Proportion of total usage"
        ]

        table_rows = []

        total_generation = sum(self.generation_totals.values())
        total_usage = sum(self.usage_data_totals.values())
        table_rows.append(["Total", total_generation/1000, total_usage/1000, f"{(1):.2%}"])

        renewable_generation = self.generation_totals["geo"] + self.generation_totals["wind"] + self.generation_totals["hydro"] + self.generation_totals["solar"]
        renewable_usage = self.usage_data_totals["geo"] + self.usage_data_totals["wind"] + self.usage_data_totals["hydro"] + self.usage_data_totals["solar"]
        table_rows.append(["  Renewable", renewable_generation/1000, renewable_usage/1000, f"{(renewable_usage/total_usage):.2%}"])

        table_rows.append(["    geo", self.generation_totals["geo"]/1000, self.usage_data_totals["geo"]/1000, f"{(self.usage_data_totals['geo']/total_usage):.2%}"])
        table_rows.append(["    wind", self.generation_totals["wind"]/1000, self.usage_data_totals["wind"]/1000, f"{(self.usage_data_totals['wind']/total_usage):.2%}"])
        table_rows.append(["    hydro", self.generation_totals["hydro"]/1000, self.usage_data_totals["hydro"]/1000, f"{(self.usage_data_totals['hydro']/total_usage):.2%}"])
        table_rows.append(["    solar", self.generation_totals["solar"]/1000, self.usage_data_totals["solar"]/1000, f"{(self.usage_data_totals['solar']/total_usage):.2%}"])

        table_rows.append(["  Non-renewable", self.generation_totals["fossil"]/1000, self.usage_data_totals["fossil"]/1000, f"{(self.usage_data_totals['fossil']/total_usage):.2%}"])
        table_rows.append(["    fossil", self.generation_totals["fossil"]/1000, self.usage_data_totals["fossil"]/1000, f"{(self.usage_data_totals['fossil']/total_usage):.2%}"])


        tabulate.PRESERVE_WHITESPACE = True
        print(tabulate.tabulate(table_rows, headers=headers, floatfmt=".2f"))

        graph.plot_usage(self.usage_data_arrays["hydro"], self.usage_data_arrays["geo"], self.usage_data_arrays["solar"], self.usage_data_arrays["wind"], self.usage_data_arrays["fossil"], self.DEMAND_POINTS)


    def report_met_demand(self):
        self.gen_status_counts["match"] += 1
        print("\033[92mDemand met\033[0m")

    def report_exceeded_demand(self, excess):
        self.gen_status_counts["excess"] += 1
        print(f"\033[91mGeneration exceeded demand! (oversupplied by {round(excess,2)})\033[0m")
        
    def report_unmet_demand(self, excess):
        self.gen_status_counts["deficit"] += 1
        print(f"\033[91mDemand not met! (undersupplied by {round(excess,2)}) \033[0m")
    
    def model_time_step(self):
        self.current_timestep_total_demand = self.DEMAND_POINTS[self.current_timestep]
        print(f"Timestep {self.current_timestep}\nDemand: {self.current_timestep_total_demand}")

        # dc1
        print("dc1")
        hydro_dc1 = self.hydro_model.hydro_model_DC1(self.current_timestep_total_demand) 
        geo_dc1 = self.available_generation_data["geo"][self.current_timestep]
        total_dc1 = hydro_dc1 + geo_dc1

        print(f"  - hydro: {hydro_dc1}")
        print(f"  - geo: {geo_dc1}")

        self.current_timestep_remaining_demand = self.current_timestep_total_demand - total_dc1

        excess = -self.current_timestep_remaining_demand
        if excess > 0:
            amount_stored = self.battery.store_power(excess)
            print(f"    (stored excess dc1-generation: {round(excess,2)})")
            if amount_stored < excess:
                self.report_exceeded_demand(excess-amount_stored)
            return

        # dc2 
        print("dc2")
        wind_useful_power, wind_leftover_power = self.wind_model.wind_model(self.current_timestep_remaining_demand, self.available_generation_data["wind"][self.current_timestep])
        self.consume_energy("wind", amount=wind_useful_power)
        
        battery_stored = self.battery.store_power(wind_leftover_power)
        print(f"  - wind-stored: {battery_stored}")
        wind_leftover_power -= battery_stored
        self.add_to_usage_data("wind", wind_leftover_power)
        self.add_to_generation_data("wind", wind_leftover_power)


        print(f"  - wind-wasted: {wind_leftover_power}" )

        self.consume_energy("solar")

        # Subtracting the dc3
        dc3 = min(0, self.current_timestep_remaining_demand)
        print(f"dc3: {round(dc3,2)}")

        # Subtracting the dc4
        dc4 = min(0, self.current_timestep_remaining_demand)
        print(f"dc4: {round(dc4,2)}")

        if self.current_timestep_remaining_demand==0:
            self.report_met_demand()
        elif self.current_timestep_remaining_demand>0:
            self.report_unmet_demand(self.current_timestep_remaining_demand)
        else:
            self.report_exceeded_demand(-self.current_timestep_remaining_demand)
        print("\n")
        
    def run_model(self):
        for self.current_timestep in range(self.NUMBER_OF_TIME_STEPS):
            self.model_time_step()
        print("MODEL DONE\n")
        self.summary_statistics()