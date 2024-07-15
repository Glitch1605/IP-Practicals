# Objectives: Write a program to sort the values of a Series object s1 in descending order of its indexes and store it into
#      series object s3.

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

s1 = pd.Series([6700, 5600, 5000, 5200], index=[1, 2, 3, 4])

s3 = s1.sort_index(ascending=False)

print("Series Object s1:")
print(s1)
print("Series Object s3:")
print(s3)