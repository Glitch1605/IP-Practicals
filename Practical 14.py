# Objectives: Write code to add plot title and axes titles to above plot.

# Software Needed: Windows 10, Python 3.12

# Coding:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(120000)
y = np.random.randn(120000)

plt.hist([y, x], bins=48, histtype="barstacked", orientation="horizontal")
plt.title("Horizontal Stackedbar Histogram")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()