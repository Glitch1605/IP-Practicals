# Objectives: Write a program to create a histogram that plots two ndarrays x and y with 48 bins, in stacked horizontal histogram.

# Software Needed: Windows 10, Python 3.12

# Coding:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(120000)
y = np.random.randn(120000)

plt.hist([y, x], bins=48, histtype="barstacked", orientation="horizontal")
plt.show()