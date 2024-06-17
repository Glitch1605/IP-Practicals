# Aim: Write a program to create a DataFrame storing salesmen details (name, zone, sales) of five salesmen.

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

SalesDict = {"Name": ["Ravi", "Dhruv", "Manan", "Vivek", "Akshay"], "Zone": ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"], "Sales": [65000, 70000, 90000, 50000, 100000]}

Sales = pd.DataFrame(SalesDict)

print(Sales)