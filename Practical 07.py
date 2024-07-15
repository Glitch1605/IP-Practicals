# Objectives: Create a following DataFrame Sales containing year wise sales figures for five salespersons in INR. Use the years
#      as column labels, and salesperson names as row labels.

#                2014     2015     2016     2017
#      Madhu     100.5    12000    20000    50000
#      Kusum     150.8    18000    50000    60000
#      Kinshuk   200.9    22000    70000    70000
#      Ankit     30000    30000    100000   80000
#      Shruti    40000    45000    125000   90000

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

SaleDict = {2014: {"Madhu": 100.5, "Kusum": 150.8, "Kinshuk": 200.9, "Ankit": 30000, "Shruti": 40000},
            2015: {"Madhu": 12000, "Kusum": 18000, "Kinshuk": 22000, "Ankit": 30000, "Shruti": 45000},
            2016: {"Madhu": 20000, "Kusum": 50000, "Kinshuk": 70000, "Ankit": 100000, "Shruti": 125000},
            2017: {"Madhu": 50000, "Kusum": 60000, "Kinshuk": 70000, "Ankit": 80000, "Shruti": 90000}}

Sales = pd.DataFrame(SaleDict)

print(Sales)