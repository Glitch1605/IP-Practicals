# Aim: Given a Series object s4. Write a program to change the values at its 2nd row (index 1) and 3rd row to 8000.

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

s4 = pd.Series([6700, 5600, 5000, 5200], index=[1, 2, 3, 4])

print("Original Series object s4:")
print(s4)

s4[1:3] = 8000

print("Series object after changing value:")
print(s4)