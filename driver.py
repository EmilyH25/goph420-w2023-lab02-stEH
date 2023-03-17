import numpy as np
import math
from math import pi
import matplotlib.pyplot as plt

from src.my_python_package.calculations.Newton_Raphson import (root_newton_raphson)
from src.my_python_package.calculations.function import (f)
from src.my_python_package.calculations.derivative import (dfdx)
from src.my_python_package.calculations.values import (calc_values)
from input_values.freq_lists import (freq_lists)
from src.my_python_package.graphs import (vel_plotter, wl_plotter)

freq, list = freq_lists()

vel_plotter
wl_plotter