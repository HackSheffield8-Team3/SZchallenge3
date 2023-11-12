from model import EnergyGrid
import scipy.optimize as optimize

def func_to_optimise(args):
    a,b,c = args
    grid = EnergyGrid(1,3000,1000, 999999999)
    grid = grid
    data = grid.run_model()
    if data[0] <=0.98:
        return 9999999999999999999999999
    else:
        return data[1]

initial_guess = [1, 500, 10000]

result = optimize.minimize(func_to_optimise, initial_guess)


if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)
