class BatteryModel():

    def __init__(self, TOTAL_STORAGE_POWER, power_stored):
        self.TOTAL_STORAGE_POWER = TOTAL_STORAGE_POWER
        self.power_stored = power_stored
        self.remaining_space = TOTAL_STORAGE_POWER - power_stored
        self.max_state_of_charge = power_stored
        

    def store_power(self, power_to_store):
        """
        stores power given. Returns the amount of power actually stored (which is less than power given if the battery does not have enough space)
        """
        storable_power = min(power_to_store, self.remaining_space)
        self.power_stored += storable_power        
        self.remaining_space = self.TOTAL_STORAGE_POWER - self.power_stored
        self.max_state_of_charge = max(self.max_state_of_charge, self.power_stored)
        return storable_power

    def get_power_stored(self):
        return self.stored_power

    def get_remaining_space(self):
        return self.remaining_space
    
    def discharge (self, requested_output):
        
        if self.power_stored >= requested_output:
            self.power_stored -= requested_output
            return requested_output
        
        if self.power_stored < requested_output:
            output = self.power_stored
            self.power_stored = 0
            return output

    


