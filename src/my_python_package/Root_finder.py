
# INITIALIZATION
import numpy as np
import math
from math import pi

def eq_1(zeta,freq):
    
    rho1 = 1800
    rho2 = 2500
    Beta1 = 1900
    Beta2 = 3200
    H = 4000
    
    under_root = H**2*(Beta1**(-2)-Beta2**(-2))-zeta**2
    tanf = np.tan(2*pi*freq*zeta)
    
    g = ((rho2/rho1)*under_root/zeta)-tanf
    
    return g
 
def vlove(zeta):
    
    H = 4000
    Beta1 = 1900
    
    love = Beta1**(-2)-(zeta/H)**2
    
    return love
    