import matplotlib.pyplot as plt
import numpy as np
from model import EnergyGrid



def plot_param_solar(start, end, step):
    cost = []
    i_list = []
    percent_fossil = []
    for i in range(start, end, step):
        i_list.append(i)
        
        grid = EnergyGrid(0, i, 0, 999999999999, NO_TEXT_OUT=True)
        
        data = grid.run_model()
        percent_fossil.append(data[0])
        cost.append(data[1])
        
    
    plt.plot(i_list, cost)
    plt.xlabel('solar param')
    plt.ylabel('cost')
    plt.show()
    
    
def plot_param_wind(start, end, step):
    cost = []
    i_list = []
    percent_fossil = []
    for i in range(start, end, step):
        i_list.append(i)
        
        grid = EnergyGrid(i, 0, 0, 999999999999, NO_TEXT_OUT=True)
        
        data = grid.run_model()
        percent_fossil.append(data[0])
        cost.append(data[1])
        
    
    plt.plot(i_list, cost)
    plt.xlabel('wind param')
    plt.ylabel('cost')
    plt.show()
    
        
def plot_param_batteries(start, end, step):
    cost = []
    i_list = []
    percent_fossil = []
    for i in range(start, end, step):
        i_list.append(i)
        
        grid = EnergyGrid(999999999999, 0, i, 999999999999, NO_TEXT_OUT=True)
        
        data = grid.run_model()
        percent_fossil.append(data[0])
        cost.append(data[1])
        
    
    plt.plot(i_list, cost)
    plt.xlabel('batteries param')
    plt.ylabel('cost')
    plt.show()
    
plot_param_solar(0, 1000000, 10000)