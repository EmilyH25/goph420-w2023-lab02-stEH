# Initialization
from math import pi
import numpy as np

def f(zeta,freq):
    """calculates the surface dispersion function value at a given zeta value and a given frequency

    Parameters
    ----------
    zeta : float
        The guess value for zeta
    freq : float
        Provided value for the frequency

    Returns
    -------
    float
        The value of the function
    """
    # provided known values of the function
    rho1 = 1800
    rho2 = 2500
    Beta1 = 1900
    Beta2 = 3200
    H = 4000
    
    # generating the function
    under_root = H**2*(Beta1**(-2)-Beta2**(-2))-zeta**2
    tanf = np.tan(2*pi*freq*zeta)
    
    g = tanf-((rho2/rho1)*(under_root)**(1/2)/zeta)
    
    return g