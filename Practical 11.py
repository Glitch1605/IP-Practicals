# Objectives: Write Python code to plot a bar chart for Inida's medal tally as shown below:
#      Also give suitable python statement to save this chart

# Software Needed: Windows 10, Python 3.12

# Coding:

import matplotlib.pyplot as plt

Category = ["Gold", "Silver", "Bronze"]
Medal = [20, 15, 18]

plt.bar(Category, Medal)
plt.ylabel("Medal")
plt.xlabel("Medal Type")
plt.title("Indian Medal tally in Olympics")
plt.show()

plt.savefig("aa.jpg")