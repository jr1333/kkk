# 1
import numpy as np

a = np.arange(1, 1001, 1)
b = np.arange(100, 11001, 10)
# 2
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

def linear_func(x, a, b):
    return a * x + b


params_a, _ = curve_fit(linear_func, a, a)
params_b, _ = curve_fit(linear_func, b, b)
fit_a = linear_func(a, *params_a)
fit_b = linear_func(b, *params_b)
# 3
import matplotlib.pyplot as plt

plt.scatter(a, a, label='Data Points a')
plt.plot(a, fit_a, 'r-', label='Fitted Curve a')
plt.scatter(b, b, label='Data Points b')
plt.plot(b, fit_b, 'g-', label='Fitted Curve b')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Data Points and Fitted Curves')
plt.show()

