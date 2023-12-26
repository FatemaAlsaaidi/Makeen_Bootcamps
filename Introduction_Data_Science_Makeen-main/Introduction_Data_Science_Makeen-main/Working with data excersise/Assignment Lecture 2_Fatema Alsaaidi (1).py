#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
df = pd.read_csv("Students Exam Scores.csv")


# In[19]:


df.head()


# # Q1

# In[20]:


df.describe()


# In[26]:


# Calculate the avg of values of Math score , reading score and writing score for every studend
avg=[]
for index, row in df.iterrows():
    total=row['MathScore']+row['ReadingScore']+row['WritingScore']
    avg.append(total/3)    
avg

df['Average Score'] = avg

# Write the DataFrame back to a CSV file
df.to_csv('output.csv', index=False)
df.head()


# In[22]:


# Get the average exam scores for each parent education type
average_scores = df.groupby('ParentEduc').mean()['Average Score']

plt.subplots(figsize=(15,5))
# Plot the average exam scores
plt.bar(average_scores.index, average_scores)
plt.xlabel('Parent Education Type')
plt.ylabel('Average Exam Score')
plt.title('Relationship Between Parent Education Type and Student Exam Scores')
plt.show()


# ##### Students whose parents have higher levels of education tend to score higher on tests. This is likely because parents with higher levels of education are more likely to provide their children with a stimulating learning environment and to help them with their homework.

# # Q2

# In[25]:


import numpy as np
from random import randint


# Generate a list of 1000 random integers between 1 and 100000
random_integers = np.random.randint(1, 100000, 1000)

# Calculate the mean and standard deviation of the list of random integers
mean = np.mean(random_integers)
print("the mean is ", mean)
std = np.std(random_integers)
print("the standard deviation is",std)

# Calculate the z-scores
z_scores = np.abs(random_integers - mean) / std

plt.subplots(figsize=(15,10))
sns.boxplot(data=df)
plt.semilogy()

# Identify the outliers
outliers = np.where(z_scores > 1.5)

# Print the outliers
print("Outliers is",outliers)


# ##### The mean of the dataset is 50788.842.The standard deviation of the dataset is 28397.50506296347. This means that the values of the dataset are typically clustered around 50788.842, but there is some variation. The outliers are all values that are less than 7 or greater than 990. This is significantly lower or higher than the average of 50788.842 for the dataset. These values ​​areoutlier s because they were incorrectly entered into the dataset.

# # Q3

# In[1]:


from random import randint

# Generate a list of 1000 random integers between 1 and 100000
random_integers00 = np.random.randint(1, 100, 10)
print("The random integres are ", random_integers00)


# In[9]:


from random import randint

# Generate a list of 1000 random integers between 1 and 100000
random_integers00 = np.random.randint(1, 100, 10)
# Print the random integers
print("The random integers are ",random_integers00)

print()

# Calculate the mean of the random integers
mean00 = np.mean(random_integers00)
print("The mean is ", mean00)

print()

# Calculate the standard deviation of the random integers
std00 = np.std(random_integers00)
print("The standare deviation is ", std00)

print()

# Standardize the random integers
standardized_integers = (random_integers00 - mean00) / std00

print()

# Print the standardized integers
print("The Standardize the random integers are ",standardized_integers)

print()
# Normalize the random integers
normalized_integers = (random_integers00 - min(random_integers00)) / (max(random_integers00) - min(random_integers00))

# Print the normalized integers
print("The Normalize the random integers are ", normalized_integers)


# ##### Here are some comments on the results :The mean of the random integers is 47.7. This means that the average value of the random integers is 47.7. The standard deviation of the random integers is 26. This means that the values of the integers are typically clustered around 47, but there is some variation. The standardized integers have a mean of 0 and a standard deviation of 1. This means that the standardized integers have been rescaled so that they have a mean of 0 and a standard deviation of 1. The normalized integers have been rescaled so that they range from 0 to 1. This means that the normalized integers can be used to compare different datasets that have different scales. Overall, the code you provided produces useful results that can be used to analyze data.

# # Q4

# In[10]:


#imported library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


df = pd.DataFrame(np.random.randint(0,100,size=(100, 2)), columns=list('xy'))
print(df.head())


# In[15]:


#draw scatter plot
plt.scatter(df['x'],df['y'])
plt.xlabel('X values')
plt.ylabel('y values')
plt.show()


# ##### The scatter plot shown as there is no relationship between values x and y

# In[ ]:




