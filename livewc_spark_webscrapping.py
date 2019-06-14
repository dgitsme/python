#!/usr/bin/env python
# coding: utf-8

# In[12]:


from bs4 import BeautifulSoup
import requests
import findspark
findspark.init('/spark24')


# In[13]:


# web scrapping
# load url
web=requests.get('https://php.net')


# In[14]:


#loading text data only for html
htmldata=web.text


# In[18]:


# now applying bs
soup=BeautifulSoup(htmldata,'html5lib')
text_only=soup.get_text()


# In[21]:


#storing data permanently
#use either one of the method for handling the file
'''f=open('php.txt','w+')
f.write(text_only)
f.close()'''


# In[23]:


#!cat php.txt
newdata=[i for i in text_only.split() ]


# In[27]:


f=open('php.txt','w')
for j in newdata:
    f.write(j)
    f.write('/n')
f.close()


# In[28]:


get_ipython().system(u'cat php.txt')


# In[ ]:




