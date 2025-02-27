# Create a scatter plot without any function encapsulation
#scatter_plt.py
import numpy as np
import matplotlib.pyplot as plt
def scatter_plt(data):
    """
    Basic Scatter Plot
    """

    plt.figure(figsize=(8, 6))
    plt.scatter(data['value1'], data['value2'], c='blue', alpha=0.5)
    plt.title('Scatter Plot of value1 vs. value2')
    plt.xlabel('value1')
    plt.ylabel('value2')
    plt.show()