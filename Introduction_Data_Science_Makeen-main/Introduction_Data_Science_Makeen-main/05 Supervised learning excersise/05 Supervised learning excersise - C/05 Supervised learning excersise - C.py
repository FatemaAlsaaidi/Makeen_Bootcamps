#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as nm
from sklearn.linear_model import LinearRegression


# In[2]:


h = nm.array([140, 150, 160, 170, 180]).reshape(-1,1)
sSize = nm.array([7,8,9,10,11])


# In[5]:


model = LinearRegression()
model.fit(h, sSize)


# In[6]:


new_size = nm.array([[145]])
per_size = model.predict(new_size)
print("Size is :", per_size[0])


# In[ ]:




