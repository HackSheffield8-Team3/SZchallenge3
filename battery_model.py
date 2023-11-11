class HydroModel ():

    def __init__(self, TOTAL_STORAGE_POWER, power_stored):
        self.TOTAL_STORAGE_POWER = TOTAL_STORAGE_POWER
        self.power_stored = potential_stored
        self.remaining_space = TOTAL_STORAGE_POWER - power_stored
        

    def store_power(power_to_store):
        """
        stores power given. Returns the amount of power it is unnable to store. If it can store all power given, returns 0.
        """
        if power_to_store <= remaining_space:
            power_stored += power_to_store
        else:
            power_stored = TOTAL_STORAGE_POWER
        
        remaining_space = TOTAL_STORAGE_POWER - power_stored
        return remaining_space

    def get_power_stored():
        return stored_power

    def get_remaining_space():
        return remaining_space

    


