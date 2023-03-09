
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
    
    g = tanf-((rho2/rho1)*(under_root)**(1/2)/zeta)
    return g
    
def dfdx(zeta, freq):    
    rho1 = 1800
    rho2 = 2500
    Beta1 = 1900
    Beta2 = 3200
    H = 4000
    
    root = (16575-(5776*(zeta**2)))**.5
    addy = 2*freq*pi/((np.cos(2*pi*freq*zeta))**2)
    deriv = (138125/(456*(zeta**2)))*(1/root)+addy
    return deriv
 
def guesses(freq):
    ini_guess = []
    n = 1
    guess = 0
    asympt = 0
    while guess < 1.69:
        nasympt = n/(4*freq)
        guess = nasympt
        if guess < 1.69:
            ini_guess.append(guess)
        n += 2
    return ini_guess
    
def newton_raphson(x0,freq,f,dfdx,eps_s=1e-8):
    eps_a = 2*eps_s
    xk = x0
    error = []
    niter = 0
    d = []
    while eps_a > eps_s:
        xn = xk-f(xk, freq)/dfdx(xk, freq)
        d.append(xn)
        eps_a = np.abs((xn-xk)/xn)
        error.append(eps_a)
        niter += 1
        xk=xn
    return xk, niter, error

