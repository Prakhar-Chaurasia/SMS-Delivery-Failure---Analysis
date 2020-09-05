#!/usr/bin/env python
# coding: utf-8

# # Reading file

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('logs-insights-results.csv')


# # Getting dates

# In[2]:


df['@timestamp'] = pd.to_datetime(df['@timestamp'])


# In[3]:


df['dates'] = df['@timestamp'].dt.date


# In[4]:


df = df.drop(['@timestamp', '@logStream'], axis = 1) 


# In[5]:


date_wise = df['dates'].value_counts()


# # Getting top 10 dates with most failures

# In[6]:


date_wise.head(10)


# # Plotting datewise failures

# In[7]:


df_daily=df.groupby('dates').agg(['count']).reset_index()
df_daily.plot(x='dates', y='delivery.destination',kind="bar")
plt.show()


# In[8]:


# Getting top 10 providers with most failures


# In[9]:


carrier_wise = df['delivery.phoneCarrier'].value_counts()


# In[10]:


carrier_wise.head(10)


# # Plotting provider wise failures

# In[11]:


df_daily=df.groupby('delivery.phoneCarrier').agg(['count']).reset_index()
df_daily.plot(x='delivery.phoneCarrier', y='delivery.destination',kind="bar")
plt.show()


# # Plotting Failure reasons

# In[12]:


df_daily=df.groupby(['delivery.providerResponse']).agg(['count']).reset_index()
df_daily.plot(x='delivery.providerResponse', y='delivery.destination',kind="bar")
plt.show()


# # Plotting Provider wise count of failure reasons

# In[13]:


table = pd.pivot_table(df, values='delivery.destination', index=['delivery.phoneCarrier'],
                   columns=['delivery.providerResponse'], aggfunc=np.count_nonzero).reset_index().fillna(0)


# In[14]:


table


# In[ ]:




