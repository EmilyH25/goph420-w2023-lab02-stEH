# Initialization
import numpy as np
import matplotlib.pyplot as plt

from src.my_python_package.calculations.Newton_Raphson import (root_newton_raphson)
from src.my_python_package.calculations.function import (f)
from src.my_python_package.calculations.derivative import (dfdx)
from src.my_python_package.calculations.values import (calc_values)
from input_values.freq_lists import (freq_lists)

freq, list = freq_lists()
zeta, vel, wl, iters = calc_values(freq, list, root_newton_raphson, f, dfdx)

count = 0
modes = []
t = 6
lbl = ['mode 1', 'mode 2', 'mode 3']

# rearranging produced lists such that they can be graphed based on modes
while count < 3:
    mode = []
    for i in range(t):
        m = i + count
        mode.append(wl[m][count])
    plt.plot(freq[count:len(freq)],mode, label = lbl[count])
    t -= 1
    count = count + 1
    
# display the graphs        
plt.legend()
plt.xlabel('frequency (Hz)')
plt.ylabel('wavelength (m)')
plt.show()