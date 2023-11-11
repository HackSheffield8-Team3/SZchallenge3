class EnergyGrid():
    def __init__(self, WIND_POWER_MULTIPLIER, INSTALLED_SOLAR_GW, MIN_HYDRO):
        self.WIND_POWER_MULTIPLIER = WIND_POWER_MULTIPLIER
        self.INSTALLED_SOLAR_GW = INSTALLED_SOLAR_GW
        self.MIN_HYDRO = MIN_HYDRO

        self.current_battery_level = 0

        with open("demand_points.txt", "r") as dp_file:
            self.DEMAND_POINTS = dp_file.readlines()
        
        self.FINAL_TIME_STEP = len(self.DEMAND_POINTS)
    
    def model_time_step(self, time):
        print(f"Time {time}\nDemand is {self.DEMAND_POINTS[time]}\n")

    def run_model(self):
        for current_time in range(self.FINAL_TIME_STEP):
            self.model_time_step(current_time)
        print("Model done")