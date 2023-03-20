import numpy as np
import math
from math import pi
import matplotlib.pyplot as plt

from src.my_python_package.calculations.Newton_Raphson import (root_newton_raphson)
from src.my_python_package.calculations.function import (f)
from src.my_python_package.calculations.derivative import (dfdx)
from src.my_python_package.calculations.values import (calc_values)
from input_values.freq_lists import (freq_lists)
from src.my_python_package.graphs import (vel_plotter, wl_plotter)

def main():
    print('successfully imported code components')
    
    
    freq, list = freq_lists()
    zeta, vel, wl, iter = calc_values(freq, list, root_newton_raphson, f, dfdx)
    
    for i in range(len(freq)):
        print('frequency value: ', freq[i])
        print('initial guess(es): ', list[i])
        print('calculated roots: ', zeta[i])
        print('each guess took ', iter[i], ' iterations')
    
    vel_plotter
    wl_plotter


main()