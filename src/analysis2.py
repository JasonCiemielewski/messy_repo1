#analysis2.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import compute_stats
from pathlib import Path

print(__file__)
current_dir = Path(__file__)
print(current_dir)


# Load data from a CSV file dumped in the repo
data = pd.read_csv('../data/data.csv')
print("Data loaded:")
print(data.head())

# Calculate some basic statistics directly in the global scope
compute_stats.compute_stats(data)

# Create a scatter plot without any function encapsulation
plt.figure(figsize=(8, 6))
plt.scatter(data['value1'], data['value2'], c='blue', alpha=0.5)
plt.title('Scatter Plot of value1 vs. value2')
plt.xlabel('value1')
plt.ylabel('value2')
plt.show()

# Some extra messy code: looping and printing out repeated info
for i in range(3):
    print("Iteration", i, "- Mean value1:", mean_value)

# Redundant code that doesn't affect anything (for demo purposes)
unused_variable = "This variable is never used!"

# Extra comments and to-do notes left in the code
# TODO: Refactor code into functions
# FIXME: Parameterize file paths and configuration settings

# End of messy script
