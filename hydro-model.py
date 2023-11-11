

# function takes total power into reservoirs, potential power stored in reservoirs, power out wanted by grid.
# returns actual output power from dams

class HydroModel ():

    def __init__(self, hydro_potential, in_power_MW, FULL_HYDRO_POTENTIAL):
        self.hydro_potential = hydro_potential
        self.in_power_MW = in_power_MW
        self.FULL_HYDRO_POTENTIAL = FULL_HYDRO_POTENTIAL





    def hydro_model_DC1(total_demand, timestep):
        
        out = total_demand * 0.2

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







    def hydro_model (in_power_MW, out_power_request):


        total = hydro_potential + in_power_MW
        if output 
        out = 0

        if (total > FULL_HYDRO_POTENTIAL):
            out = max(out_power_request, in_power_MW)
        elif ((hydro_potential-out_power_request) >= 0):
            out = out_power_request
        else:
            out = total

        hydro_potential = total - out
        return (out)




        final_total = total - out

