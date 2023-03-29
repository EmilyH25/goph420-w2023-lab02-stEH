# INITIALIZATION
import numpy as np
import math
from math import pi
import matplotlib.pyplot as plt
from src.my_python_package.calculations.Newton_Raphson import (root_newton_raphson)
from src.my_python_package.calculations.function import (f)
from src.my_python_package.calculations.derivative import (dfdx)


def calc_values(frequencies, listfreq, root, f, dfdx):
    """presents results from newton raphson function in the form of lists, calculates the love wave velocity and wavelength for each calculated value

    Parameters
    ----------
    frequencies : list
        List of the frequencies of interest
    listfreq : list
        Initial guesses for each frequency
    root : function
        root finding function
    f : function
        the equation of interest, in the form that can be applied to the root finding methods
    dfdx: function
        the derivative of the equation of interest

    Returns
    -------
    zeta_list : list
        list of calculated roots for each frequency
    vel_list : list
        list of calculated velocity for each frequency
    wl_list : list
        list of calculated wavelengths for each frequency
    b_list : list
        list recording the number of iterations to find each root
    """
    
    zeta_list = []
    b_list = []
    e_list = []
    # record root and the number of iterations required
    for i in range (len(frequencies)):
        
        small_list = []
        smb_list = []
        sme_list =[]
        
        for t in range (len(listfreq[i])):
            zet, iter, error = root(listfreq[i][t],frequencies[i],f,dfdx)
            small_list.append(zet)
            smb_list.append(iter)
            sme_list.append(error)
        
        zeta_list.append(small_list)
        b_list.append(smb_list)
        e_list.append(error)
    
    vel_list = []
    
    # calculate and record the velocities from calculated root values
    for i in range (len(frequencies)):
        
        small_list = []
        
        for t in range (len(zeta_list[i])):
            cl = (1/((1/1900)**2-((zeta_list[i][t])/4000)**2))**(0.5)
            small_list.append(cl)
            
        vel_list.append(small_list)
	
    wave_list = []
    
    # calculate and record the wavelength from calculated velocity values
    for i in range (len(frequencies)):
    
        small_list = []
        
        for t in range (len(vel_list[i])):
            wave = (vel_list[i][t])/frequencies[i]
            small_list.append(wave)
            
        wave_list.append(small_list)
        
    return zeta_list, vel_list, wave_list, b_list, e_list