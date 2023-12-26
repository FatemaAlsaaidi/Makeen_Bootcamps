#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import accuracy_score


# In[22]:


#Generate a random dataset with two features (x1, x2)
DIM = 20      # number iof features (dimension)
CLASSES = 4   # number of classes
N = 1000      #number of samples
X, y = make_blobs(n_samples = N, centers = CLASSES, n_features = DIM, cluster_std=3)

np.unique(y)

np.max(X, axis=0)
X[:,2] = X[:,2]*1000
X[:,4] = X[:,4]*10000
X[:,15] = X[:,15]*100


# In[24]:


#Divide the dataset into training and test sets. 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
print(X_train.shape, X_test.shape)


# In[25]:


#Implement the KNN classification.
k=knn(n_neighbors=2)


# In[26]:


k.fit(X_train,y_train)


# In[27]:


y_pred=k.predict(X_test)


# In[28]:


accuracy = accuracy_score(y_pred, y_test)
accuracy


# In[29]:


# Train the KNN classifier on the training set and determine the optimal value of k using 
#cross-validation. You can use a library like Scikit-learn to perform cross-validation and select the 
#optimal value of k
k_={'n_neighbors':[1,2,3,4,5,6,7,8,9,10,11,12]}


# In[30]:


cv = GridSearchCV(k,k_,  refit = True, verbose = 3,n_jobs=-1) #to find the best k


# In[31]:


cv.fit(X_train, y_train) 


# In[32]:


print(cv.best_params_) 


# In[33]:


k2=knn(n_neighbors=3)
k2.fit(X_train, y_train)
y_pred2=k2.predict(X_test)
accuracy2 = accuracy_score(y_pred2, y_test)
accuracy2


# In[ ]:




