
# INITIALIZATION
import numpy as np
import math
from math import pi
import matplotlib.pyplot as plt

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
        zet, iter, error = newton_raphson(list[i][t],frequencies[i],f,dfdx)
        small_list.append(zet)
    zeta_list.append(small_list)

vel_list = []
for i in range (len(frequencies)):
    small_list = []
    for t in range (len(zeta_list[i])):
        cl = (1/((1/1900)**2-((zeta_list[i][t])/4000)**2))**(0.5)
        plt.plot(frequencies[i],cl,'g^')
        small_list.append(cl)
    vel_list.append(small_list)
plt.xlabel('frequency (Hz)')
plt.ylabel('velocity (m/s2)')
plt.show()    

wave_list = []
for i in range (len(frequencies)):
    small_list = []
    for t in range (len(vel_list[i])):
        wave = (vel_list[i][t])/frequencies[i]
        plt.plot(frequencies[i], wave, 'bo')
        small_list.append(wave)
    wave_list.append(small_list)
plt.xlabel('frequency (Hz)')
plt.ylabel('wavelength (m)')
plt.show()