# Aim: Given a Series that stores the area of some states in km^2. Write code to find out the biggest and smallest three 
#      area from the given Series. Given Series has been created like this :

# Ser1 = pd.Series([34567, 890, 450, 67892, 34677, 78902, 256711, 678291, 637632, 25723, 2367, 11789, 345, 256517])

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

Ser1 = pd.Series([34567, 890, 450, 67892, 34677, 78902, 256711, 678291, 637632, 25723, 2367, 11789, 345, 256517])

print("Top 3 biggest areas are:")
print(Ser1.sort_values().tail(3))
print("Top 3 smallest areas are:")
print(Ser1.sort_values().head(3))