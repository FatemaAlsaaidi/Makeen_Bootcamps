#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[2]:


df=pd.read_csv('Supervised learning excersise-B.csv')
df


# In[3]:


clf = tree.DecisionTreeClassifier()


# In[5]:


x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values


# In[6]:


x


# In[7]:


y


# In[8]:


df2=df.copy()
df2['Loan Term'] = df2['Loan Term'].astype('category')
df2['Loan Term'] = df2['Loan Term'].cat.codes
df2


# In[9]:


df2['Employment Status'] = df2['Employment Status'].astype('category')
df2['Employment Status'] = df2['Employment Status'].cat.codes
df2


# In[10]:


df2['Previous Delinquencies'] = df2['Previous Delinquencies'].astype('category')
df2['Previous Delinquencies'] = df2['Previous Delinquencies'].cat.codes
df2


# In[11]:


df2['Approved'] = df2['Approved'].astype('category')
df2['Approved'] = df2['Approved'].cat.codes
df2


# In[12]:


x = df2.iloc[:,:-1].values
y = df2.iloc[:,-1].values


# In[13]:


clf.fit(x,y)


# In[14]:


tree.plot_tree(clf)


# In[15]:


clf.score(x,y)


# In[ ]:




