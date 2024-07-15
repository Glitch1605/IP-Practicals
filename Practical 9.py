# Objectives: Four dictionaries store the details of four employees-of-the-month as (empno, name). Write a program to create
#      a dataframe from these.

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

Emp1 = {"EmpNo": 101, "Name": "Rohit"}
Emp2 = {"EmpNo": 102, "Name": "Rahul"}
Emp3 = {"EmpNo": 103, "Name": "Rishab"}
Emp4 = {"EmpNo": 104, "Name": "Rinku"}

df = pd.DataFrame([Emp1, Emp2, Emp3, Emp4])

print(df)