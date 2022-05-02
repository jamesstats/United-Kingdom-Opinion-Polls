#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd


# In[2]:


u_k='https://en.wikipedia.org/wiki/Opinion_polling_for_the_next_United_Kingdom_general_election' 


# In[3]:


polls = pd.read_html(u_k)  #reading the html 


# In[24]:


westminster=polls[1] #chosing the first table


# In[5]:


westminster.rename(columns={'Datesconducted':'Date'},inplace=True) #rename the column to wards


# In[6]:


westminster.drop('Samplesize',inplace=True, axis=1) #deleting unwanted columns
westminster.drop('Reform', inplace=True, axis=1)
westminster.drop('Client', inplace=True, axis=1)
westminster.drop('Others', inplace=True, axis=1) 


# In[7]:


westminster.columns=[multicols[-1] for multicols in westminster.columns] #deleting the extra column header


# In[8]:


westminster.rename(columns={'Unnamed: 5_level_1':'Cons','Unnamed: 6_level_1':'Lab','Unnamed: 7_level_1':'LibDems','Unnamed: 8_level_1':'SNP','Unnamed: 9_level_1':'Greens'},inplace=True) #rename the column to wards


# In[27]:


westminster=westminster.drop(labels=[47],axis=0) #deleting unwanted rows by index number a.k.a row number


# In[30]:


westminster=westminster.drop(labels=[70],axis=0) #deleting unwanted rows by index number a.k.a row number


# In[33]:


westminster.to_csv("all_polls.csv", index=False) 

