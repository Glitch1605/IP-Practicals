# Objectives: Write a program to create a Series object with 6 random integers and having indexes as : ["p", "q", "r", "n", "t", "v"].

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd
import numpy.random as rd

Ser1 = pd.Series(rd.randint(6, size=6), index=["p", "q", "r", "n", "t", "v"])

print(Ser1)