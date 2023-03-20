# Initialization
from math import pi
import numpy as np

def dfdx(zeta, freq):
    """calculates the value of the derivative of the surface dispersion function at a given zeta value and a given frequency

    Parameters
    ----------
    zeta : float
        The guess value for zeta
    freq : float
        Provided value for the frequency

    Returns
    -------
    float
        The value of the derivative
    """
    # provided known values of the function
    rho1 = 1800
    rho2 = 2500
    Beta1 = 1900
    Beta2 = 3200
    H = 4000
    
    # generating the derivative of the function
    root = (16575-(5776*(zeta**2)))**.5
    addy = 2*freq*pi/((np.cos(2*pi*freq*zeta))**2)
    deriv = (138125/(456*(zeta**2)))*(1/root)+addy
    
    return deriv