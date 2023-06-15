#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_csv('Book3.csv')


# In[3]:


dataset


# In[4]:


y = dataset['Salary']


# In[5]:


x = dataset['Years Experience']


# In[6]:


x.shape


# In[7]:


x.values


# In[9]:


X = x.values.reshape(14,1)


# In[10]:


X.ndim


# In[11]:


from sklearn.linear_model import LinearRegression


# In[12]:


model = LinearRegression()


# In[14]:


model.coef_


# In[13]:


model.fit(X,y)


# In[15]:


model.predict([[3.5]])


# In[16]:


c = 56846


# In[19]:


import matplotlib.pyplot as plt


# In[20]:


plt.scatter(X,y)


# In[ ]:




