"""
class documentation
"""
class HydroModel ():

    def __init__(self, hydro_potential, in_power_MW, FULL_HYDRO_POTENTIAL):
        self.hydro_potential = hydro_potential
        self.in_power_MW = in_power_MW
        self.FULL_HYDRO_POTENTIAL = FULL_HYDRO_POTENTIAL





    def hydro_model_DC1(total_demand, timestep):
        """
        func documentation
        """
        out = total_demand * 0.2
        hydro_potential = hydro_potential + in_power_MW
        # if hydro can provide enough power, give the power
        if (hydro_potential >= out):
            hydro_potential = hydro_potential - out
            out = out
        else:
            # else, give what power it can and report an error
            out = hydro_potential
            hydro_potential = 0
            print(f"ERROR!!! AT {timestep}. HYDRO CANNOT PROVIDE ENOUGH POWER IN DC1")
        return (out)








    def hydro_model_DC3 (out_power_request):
        """
        func documentation
        """
        expected_potential = hydro_potential - out_power_request

        if (expected_potential < 0):
            out = hydro_potential
            expected_potential = 0
        else:
            hydro_potential = expected_potential
            out = out_power_request
    



        final_total = total - out

