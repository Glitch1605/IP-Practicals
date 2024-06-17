# Aim: Write a program to create a data series and then change the indexes of the Series object in any random order.

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

Ser1 = pd.Series([100, 200, 300, 400, 500], index = ["I", "J", "K", "L", "M"])

print("Original Data Series:")
print(Ser1)

Ser1 = Ser1.reindex(index=["K", "I", "M", "L", "J"])

print("Data Series after changing the order of index:")
print(Ser1)