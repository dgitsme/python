#!/usr/bin/env python
# coding: utf-8

# In[24]:


import time
import matplotlib.pyplot as plt
import findspark
findspark.init('/spark24')


# In[27]:


from pyspark import SparkContext
sc=SparkContext()


# In[12]:


rdd=sc.textFile('a.txt')


# In[13]:


wc=rdd.flatMap(lambda line:line.split(" ")).map(lambda word:(word,1)).reduceByKey(lambda x,y:x+y)


# In[7]:


data=wc.collect()


# In[20]:


list1=[]
list2=[]
for i in data:
    list1.append(i[0])
    list2.append(i[1])


# In[26]:


plt.figure(figsize=(12,6))
plt.xlabel('words')
plt.ylabel('count')
plt.grid()
plt.bar(list1,list2)


# In[ ]:




