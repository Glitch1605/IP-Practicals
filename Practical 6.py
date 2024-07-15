# Objectives: Given a DataFrame df:

#         Age     Name     Weight
#      0  15      Arnav    42
#      1  22      Charles  75
#      2  35      Guru     66

#      Write a program to display only the Weight of first and thrid rows.

# Software Needed: Windows 10, Python 3.12

# Coding:

import pandas as pd

df = pd.DataFrame({"Age": [15, 22, 35], "Name": ["Arnav", "Charles", "Guru"], "Weight": [42, 75, 66]})

print(df)
print(df.iloc[[0, 2], [2]])