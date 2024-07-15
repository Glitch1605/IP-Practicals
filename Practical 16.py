# Objectives: Write a program to draw line charts from the given financial data of ABC Co, for 5 days in the form of a DataFrame
#      namely fdf as shown below:

#            Day1     Days2     Days3     Day4     Day5
#      0     74.25    56.03     59.30     69.00    89.65
#      1     76.06    68.71     72.07     78.47    79.65
#      2     69.50    62.89     77.65     65.53    80.75
#      3     72.55    56.42     66.46     76.85    85.08

# Software Needed: Windows 10, Python 3.12

# Coding:

import matplotlib.pyplot as plt
import pandas as pd

data = {"Day1": [74.25, 76.06, 69.50, 72.55], "Day2": [56.03, 68.71, 62.89, 56.42], "Day3": [59.30, 72.07, 77.65, 66.46],
        "Day4": [69.00, 78.47, 65.53, 76.85], "Day5": [89.65, 79.65, 80.75, 85.08]}

df = pd.DataFrame(data)

df.plot()
plt.show()