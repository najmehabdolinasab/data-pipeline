#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

def transform_and_standardize(data):
    # Filter out non-positive values as log is not defined for them
    positive_data = [x for x in data if x > 0]
    
    # Step 1: Apply the natural logarithm to each data point
    log_data = np.log(positive_data)
    
    # Step 2: Calculate mean and standard deviation of the log-transformed data
    mean_log = np.mean(log_data)
    std_log = np.std(log_data)
    
    # Step 3: Standardize the log-transformed data
    standardized_data = (log_data - mean_log) / std_log
    
    # Round the numbers to two decimal places
    standardized_data = np.round(standardized_data, 2)
    
    return standardized_data

# Example usage
data = [1, 1, 2, 3, 4, 5, 50, 100, 40, 300, -300]
print(transform_and_standardize(data))


# In[ ]:




