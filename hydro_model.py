"""
class documentation
"""
class HydroModel ():

    def __init__(self, hydro_potential, input_potential, FULL_HYDRO_POTENTIAL):
        self.hydro_potential = hydro_potential
        self.input_potential = input_potential
        self.FULL_HYDRO_POTENTIAL = FULL_HYDRO_POTENTIAL





    def hydro_model_DC1(self, total_demand):
        """
        func documentation
        """
        output_requested = float(total_demand) * 0.20 # 20% of demand
        self.hydro_potential += self.input_potential # water flows in
        expected_potential = self.hydro_potential - output_requested # expected potential in reservoir - can be negative
        self.hydro_potential = max(expected_potential, 0) # hydro potential is set to expected potential bound to 0+
        output_actual = output_requested + min(expected_potential, 0) 
        # if the requested output cannot be fully provided, the potential that could not be generated is removed from the requested amount

        """
        if (hydro_potential >= out): # give power 
            hydro_potential -= out
            # out = out ()
        else:
            # else, give what power it can and report an error
            out = hydro_potential
            hydro_potential = 0
            print("ERROR: HYDRO CANNOT PROVIDE ENOUGH POWER IN DC1")
        """
        return output_actual








    def hydro_model_DC3 (self, out_power_request):
        """
        func documentation
        """
        expected_potential = hydro_potential - output_requested
    
        # something

    def hydro_model_remove_overflow ():
        hydro_potential = min(hydro_potential, FULL_HYDRO_POTENTIAL)