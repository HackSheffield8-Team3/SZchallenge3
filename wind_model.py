class WindModel ():
    def wind_model(self, requested_output, actual_output, available_storage_capacity):
        #if demand less than wind energy output, useful power is total requested output and leftover is remaining wind energy
        if requested_output < actual_output:
            used = requested_output
            leftover_power = actual_output - useful_power
        #if demand greater than/equal to wind energy output, useful power is all wind energy at timestamp and leftover is zero
        else:
            used = actual_output
            leftover_power = 0
        
        stored  = min(leftover_power, available_storage_capacity)
        wasted = leftover_power - stored

        return [used, stored, wasted]