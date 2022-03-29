#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = [1,2,3,4]


# In[2]:


type(lst)


# In[3]:


type(lst[0])


# In[4]:


lst = lst + [3.14,2.71,4.6]


# In[5]:


lst


# In[6]:


st = ['ucp','pakistan']


# In[7]:


lst = lst + st


# In[8]:


lst


# In[9]:


lst.extend([5,4,3])


# In[10]:


lst


# In[11]:


lst.insert(5,213)


# In[12]:


lst


# In[13]:


lst.append(['umt','uet'])


# In[14]:


lst


# In[15]:


lst[-1]


# In[17]:


lst[-1][1]


# In[18]:


lst[-1][1][2]


# In[19]:


#deletion

del lst[5]


# In[20]:


lst


# In[22]:


lst.remove('pakistan')


# In[23]:


lst


# In[25]:


lst.pop()


# In[26]:


lst


# In[27]:


lst.sort()


# In[28]:


lst.remove('ucp')


# In[29]:


lst.sort()


# In[30]:


lst


# In[34]:


lst.sort(reverse=True)


# In[35]:


lst


# In[36]:


# Dictionary
dict={
    'jafar':'boy',
    'ucp':'university'
}


# In[39]:


dict


# In[40]:


d = {'Country':['Pakistan','Iran','India','Afghanistan','China'],
    'Capital':['IslamAbad','Tehran','Dehli','Kabul','Bejing'],
    'Population':[24.5,22.7,135.8,5.3,175.2]
    }


# In[41]:


type(d)


# In[42]:


d


# In[44]:


d.keys()


# In[45]:


d.values()


# In[46]:


d.items()


# In[47]:


for k in d.keys():
    print(k)


# In[48]:


for v in d.values():
    print(v)


# In[49]:


for k,v in d.items():
    print(k,' => ',v)


# In[50]:


import pandas as pd


# In[51]:


df = pd.DataFrame.from_dict(d)


# In[52]:


df


# In[53]:


df.to_csv('pbd_d3.csv',index=False, header=True)


# In[54]:


dff = pd.read_csv('pbd_d3.csv')


# In[55]:


dff.head()


# In[57]:


dff.tail(3)


# In[59]:


dff.shape


# In[60]:


dff.describe()


# In[61]:


# tupple
t = (1,2,3,4)


# In[62]:


type(t)


# In[64]:


t[0:3]


# In[65]:


t[1]


# In[66]:


t = t +(55,66,77)


# In[67]:


t


# In[69]:


lst


# In[71]:


t = t + tuple(lst)


# In[72]:


t


# In[ ]:




