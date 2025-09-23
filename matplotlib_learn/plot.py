# what is matplotlib ?
# ----> matplolib is a library in python used to create static, animated , interactive plots.

# main  module is : pyplot ---provides function to make plots just like MATLAB

# PLOTS

import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,25,30]
plt.plot(x,y)
plt.title("simple Line plots")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()