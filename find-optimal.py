from model import EnergyGrid

best_cost = 0
best_ijk = [0,0,0]
for i in range(1, 3):
    for j in range(1, 3):
        for k in range(1, 3):
            grid = EnergyGrid(i,j,k, 999999999999)
            grid = grid
            
            # assume grid.run_model() returns [fraction renewable, cost]
            data = grid.run_model()
            if data[0] >=0.98:
                if data[1] <= best_cost:
                    best_cost = data[1]
                    best_ijk = [i,j,k]
            #store the best i,j,k so far based on cost
            #when done, output the stored value

print(str(best_cost))
print(str(best_ijk[0]))
print(str(best_ijk[1]))
print(str(best_ijk[2]))
