"""
class documentation
"""
class HydroModel ():

    def __init__(self, hydro_potential, input_potential, FULL_HYDRO_POTENTIAL):
        self.hydro_potential = hydro_potential
        self.input_potential = input_potential
        self.FULL_HYDRO_POTENTIAL = FULL_HYDRO_POTENTIAL


    def hydro_model_output_request(self, output_requested):
        expected_potential = self.hydro_potential - output_requested # expected potential in reservoir - can be negative
        self.hydro_potential = max(expected_potential, 0) # hydro potential is set to expected potential bound to 0+
        output_actual = output_requested + min(expected_potential, 0) 
        # if the requested output cannot be fully provided, the potential that could not be generated is removed from the requested amount


    def hydro_model_remove_overflow ():
        self.hydro_potential = min(hydro_potential, FULL_HYDRO_POTENTIAL)


    def hydro_model_DC1(self, total_demand):
        self.hydro_potential += self.input_potential # water flows in
        return hydro_model_output_request(float(total_demand) * 0.20) # request 20% of demand


    def hydro_model_DC3 (self, output_requested):
        hydro_model_output_request(self, output_requested)
