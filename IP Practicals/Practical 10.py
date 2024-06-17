# Aim: A list stores three dictionaries each storing details, (old price, new price, change). Write a program to create
#      a dataframe from it

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

list = [{"Old Price": 2400, "New Price": 2500, "Change": 100}, {"Old Price": 1750, "New Price": 1900, "Change": 150}, {"Old Price": 2000, "New Price": 2500, "Change": 500}]

df = pd.DataFrame(list)

print(df)