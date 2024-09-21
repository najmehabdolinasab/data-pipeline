#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def detect_outlier(data):
    # Calculate mean and standard deviation
    mean = np.mean(data)
    std_dev = np.std(data)
    
    # Determine the range for normal data
    lower_bound = mean - 1.5 * std_dev
    upper_bound = mean + 1.5 * std_dev
    
    # Detect outliers
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    
    return outliers

# Example usage
print(detect_outlier([1, 1, 2, 3, 4, 5, 50, 100, 40, 300, -300]))


# In[ ]:




