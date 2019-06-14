#!/usr/bin/env python
# coding: utf-8

# In[12]:


import findspark
findspark.init('/spark24')


# In[17]:


# now calling pyspark
from pyspark import SparkContext
sc=SparkContext()


# In[18]:


# loading file
frdd=sc.textFile('a.txt')


# In[22]:


#applying mapping function
[i for i in dir(frdd) if 'flat' in i]


# In[27]:


# splitting in line
linesplit=frdd.flatMap(lambda line:line.split(" "))
        #for line in frdd.flatMap
           #   line.split(" ")


# In[31]:


# applying mapping
#dir(linesplit)
mapping=linesplit.map(lambda word: (word,1))


# In[32]:


#now applying reduce
count=mapping.reduceByKey(lambda a,b:a+b)


# In[35]:


count.collect()


# In[ ]:




