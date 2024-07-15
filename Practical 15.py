# Objectives: A company randomly generates a weekly wining number (between 0..100) for 10 weeks. An employee of the company wants
#      to plot the sine values of winning numbers (nump.sin() function) on a line chart. Write a program to help him
#      accomplish this.

# Software Needed: Windows 10, Python 3.12

# Coding:

import matplotlib.pyplot as plt
import numpy as np

ar1 = np.random.randint(100, size=10)

sinar = np.sin(ar1)

plt.plot(ar1, sinar)
plt.xlabel("Weekly Numbers")
plt.ylabel("Sine Values")
plt.show()