# Calculate some basic statistics directly in the global scope
import numpy as np

def compute_stats(data):
    """
    compute statistics
    """
 
    mean_value = data['value1'].mean()
    std_value = data['value1'].std()
    print("Mean of value1:", mean_value)
    print("Standard deviation of value1:", std_value)