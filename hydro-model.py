

# function takes total power into reservoirs, potential power stored in reservoirs, power out wanted by grid.
# returns actual output power from dams, potential pwoer stored in reservoirs

class HydroModel ();

    def __init__():

    def hydro_model (in_power_MW, hydro_potential, out_power_request):
        FULL_HYDRO_POTENTIAL = 10_000_000

        if (hydro_potential == FULL_HYDRO_POTENTIAL):



            return (out_power_MW, hydro_potential)

        if (hydro_potential < 0.2 * FULL_HYDRO_POTENTIAL):
            return(0)


