#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[5]:


df1 = pd.read_csv('Desktop/IR_water.csv',header =None)


# In[6]:


df1


# In[4]:


df1[1] = df1[1]*100


# In[5]:


df1


# In[10]:


cm = df1[0]
T = df1[1]


# In[9]:


fig = plt.figure()
axes = fig.add_axes([1,1,1,1])

axes.plot(cm,T, label = 'IR_WATER')



axes.set_title('Title')
axes.set_ylabel('T(%)')
axes.set_xlabel('cm-1')

axes.legend()


# In[7]:


df = pd.read_csv('Desktop/FSO15_IR_cleaned.csv',header =None)


# In[12]:


df


# In[13]:


df[0]


# In[8]:


cm1 = df[1]
T1 = df[2]


# In[28]:


fig = plt.figure()
axes = fig.add_axes([1,1,1,1])

axes.plot(cm1,T1/max(T1)*100, label = 'IR_FSO15')
axes.plot(cm,T*100/max(T), label = 'IR_WATER')


axes.set_title('IR_SPECTRUM')
axes.set_ylabel('T(%)')
axes.set_xlabel('Wavelength cm$^{-1}$')
axes.set_xlim(4000,400)

axes.legend()


# In[30]:


fig = plt.figure()
axes = fig.add_axes([1,1,1,1])

axes.plot(cm1,T1/max(T1)*100, label = 'IR_FSO15')

axes.set_title('Title')
axes.set_ylabel('T(%)')
axes.set_xlabel('Wavelength cm$^{-1}$')

axes.set_xlim(4000,400)
axes.set_ylim(80,105)
axes.legend()


# In[ ]:




