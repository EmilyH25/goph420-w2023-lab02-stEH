# INITIALIZATION
import numpy as np
import math
from math import pi
import matplotlib.pyplot as plt
from src.my_python_package.calculations.Newton_Raphson import (root_newton_raphson)
from src.my_python_package.calculations.function import (f)
from src.my_python_package.calculations.derivative import (dfdx)


def calc_values(frequencies, list, root, f, dfdx):
    zeta_list = []
    for i in range (len(frequencies)):
        small_list = []
        for t in range (len(list[i])):
            zet, iter, error = root_newton_raphson(list[i][t],frequencies[i],f,dfdx)
            small_list.append(zet)
        zeta_list.append(small_list)
    
    vel_list = []
    for i in range (len(frequencies)):
        small_list = []
        for t in range (len(zeta_list[i])):
            cl = (1/((1/1900)**2-((zeta_list[i][t])/4000)**2))**(0.5)
            small_list.append(cl)
        vel_list.append(small_list)
	
    wave_list = []
    for i in range (len(frequencies)):
        small_list = []
        for t in range (len(vel_list[i])):
            wave = (vel_list[i][t])/frequencies[i]
            small_list.append(wave)
        wave_list.append(small_list)
    return zeta_list, vel_list, wave_list