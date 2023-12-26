#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import library
import pandas as pd
from sklearn.metrics import mean_squared_error,accuracy_score


# In[2]:


#create the data frame
data={'Size (sq ft)':[1000,1500,2000,2500,3000],
     'Price(OMR)': [15000,25000,35000,45000,55000],
     'predicted_Price':[14500,26500,33000,44500,60000]}
df=pd.DataFrame(data)
df


# In[3]:


# Calculate the mean squared error (MSE) of the modeL
mean_squared_error(df['Price(OMR)'],df['predicted_Price'])


# In[4]:


accu=0
for a in df['Price(OMR)']:
    for p in df['predicted_Price']:
        if (p<=1.1*a) or (p>=0.9*a):
            accu+=1
accu


# In[5]:


err=100-accu
err


# In[ ]:




