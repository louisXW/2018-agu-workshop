#!/usr/bin/env python
# coding: utf-8

# # Example data analysis notebook
# 
# This notebook downloads and analyses some surface air temperature anomaly data from [Berkeley Earth](http://berkeleyearth.org/).

# Import the required libraries.

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import requests


# Use the [requests](http://docs.python-requests.org/) library to download the data file for Australia.

# In[12]:


# Define the URL
url = 'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/australia-TAVG-Trend.txt'
# Download the content of the URL
response = requests.get(url)
# Save it to a file
with open("data.txt", 'w') as open_file:
    open_file.write(response.text)


# Load the data using numpy (skip the header records which are marked with a `%`).

# In[6]:


data = np.loadtxt("data.txt", comments="%")


# Extract the monthly temperature anomaly and calculate an approximate "decimal year" to use in plotting.

# In[7]:


decimal_year = data[:, 0] + 1/12*(data[:, 1] - 1)
temperature_anomaly = data[:, 2]


# Plot the data so we can see what it's like.

# In[8]:


plt.figure(figsize=(10, 6))
plt.title("Temperature anomaly for Australia")
plt.plot(decimal_year, temperature_anomaly)
plt.xlabel('year')
plt.ylabel('temperature anomaly (C)')
plt.grid()
plt.xlim(decimal_year.min(), decimal_year.max())


# The data are kind of noisy at this scale so let's calculate a 12-month moving average for a smoother time series.

# In[10]:


moving_avg = np.full(temperature_anomaly.size, np.nan)
for i in range(6, moving_avg.size - 6):
    moving_avg[i] = np.mean(temperature_anomaly[i - 6:i + 6])


# In[11]:


plt.figure(figsize=(10, 6))
plt.title("Temperature anomaly for Australia")
plt.plot(decimal_year, temperature_anomaly, label="anomaly")
plt.plot(decimal_year, moving_avg, label="12-month moving average", linewidth=3)
plt.xlabel('year')
plt.ylabel('temperature anomaly (C)')
plt.legend()
plt.grid()
plt.xlim(decimal_year.min(), decimal_year.max())


# In[ ]:


moving_avg = np.full(temperature_anomaly.size, np.nan)
for i in range(6, moving_avg.size - 6):
    moving_avg[i] = np.mean(temperature_anomaly[i - 6:i + 6])

