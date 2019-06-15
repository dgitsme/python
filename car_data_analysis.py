#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# In[16]:


url="Downloads/car.data"


# In[17]:


df=pd.read_csv(url,header =None)


# In[18]:


df.head(5)


# In[19]:


headers=["class","buying","maint","doors","persons","lug_boot","safety"]


# In[20]:


df.columns=headers


# In[21]:


df.head(5)


# In[22]:


path="/home/divyansh/Desktop/final.csv"


# In[11]:


df.to_csv(path)


# In[ ]:




