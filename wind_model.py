class WindModel ():
    def wind_model(self, requested_output, actual_output, available_battery_storage_capacity):
        #if demand less than wind energy output, useful power is total requested output and leftover is remaining wind energy
        if requested_output < actual_output:
            useful_power = requested_output
            leftover_power = actual_output - useful_power
        #if demand greater than/equal to wind energy output, useful power is all wind energy at timestamp and leftover is zero
        else:
            useful_power = actual_output
            leftover_power = 0

        return [useful_power, leftover_power]