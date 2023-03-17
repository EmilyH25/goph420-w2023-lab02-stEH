# INITIALIZATION
import numpy as np
import math
from math import pi
import matplotlib.pyplot as plt


frequencies = [0.1,0.5,1,1.5,2,2.5]
f1_g = [1.4]
f2_g = [0.4,1.25]
f3_g = [0.23,0.7,1.15]
f4_g = [0.159, 0.47, 0.79]
f5_g = [0.12,0.36,0.6]
f6_g = [0.099,0.299,0.48]

list = [f1_g,f2_g,f3_g,f4_g,f5_g,f6_g]


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