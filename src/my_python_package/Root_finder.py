
# INITIALIZATION
import numpy as np
import math
from math import pi

def f(zeta,freq):
    
    rho1 = 1800
    rho2 = 2500
    Beta1 = 1900
    Beta2 = 3200
    H = 4000
    
    under_root = H**2*(Beta1**(-2)-Beta2**(-2))-zeta**2
    tanf = np.tan(2*pi*freq*zeta)
    
    g = ((rho2/rho1)*(under_root)**(1/2)/zeta)-tanf
    return g
    
def dfdx(zeta, freq):    
    rho1 = 1800
    rho2 = 2500
    Beta1 = 1900
    Beta2 = 3200
    H = 4000
    
    dens_ratio = rho1/rho2
    under_root = H**2*(Beta1**(-2)-Beta2**(-2))-zeta**2
    tanf = np.tan(2*pi*freq*zeta)
    
    deriv = dens_ratio*((-1/(under_root**0.5))-(under_root**0.5)/zeta**2)-((2*freq*pi)/(np.cos(2*pi*freq*zeta)))
    return deriv
 
 
 
def newton_raphson(x0,f,dfdx,freq,eps_s=1e-8):
    eps_a = 2*eps_s
    xk = x0
    while eps_a > eps_s:
        dx = -f(xk, freq)/dfdx(xk, freq)
        xk += dx
        eps_a = np.abs(dx/xk)
    return xk