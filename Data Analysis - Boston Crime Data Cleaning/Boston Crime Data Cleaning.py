#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


crime = pd.read_csv('crime.csv')


# In[3]:


crime


# In[4]:


crime.isnull()


# In[5]:


crime.isnull().any(axis=1)


# In[8]:


rows_with_missing_values = crime.isnull().any(axis=1)
crime[rows_with_missing_values]


# In[11]:


cleaned_crimes = crime.drop(columns=['YEAR','MONTH','HOUR'])


# In[12]:


cleaned_crimes


# In[13]:


cleaned_crimes['OFFENSE_CODE_GROUP'].unique()


# In[14]:


cleaned_crimes['OFFENSE_DESCRIPTION'].unique()


# In[15]:


cleaned_crimes['STREET'].unique()


# In[16]:


cleaned_crimes['DAY_OF_WEEK'].unique()


# In[21]:


cleaned_crimes = cleaned_crimes.drop(columns=['Location'])


# In[22]:


cleaned_crimes


# In[ ]:




