# Objectives: Write a program to plot a chart based on the given data to depict the changing weekly
#      average temperature in Delhi for four weeks.

#      Week = [1, 2, 3, 4]
#      Avg_week_temp = [40, 42, 38, 44]

# Software Needed: Windows 10, Python 3.12

# Coding:

import matplotlib.pyplot as plt

Week = [1, 2, 3, 4]
Avg_week_temp = [40, 42, 38, 44]

plt.plot(Week, Avg_week_temp)
plt.show()