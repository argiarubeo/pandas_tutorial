#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


df = pd.read_csv('data/survey_results_public_cut.csv')


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


schema_df = pd.read_csv('data/survey_results_schema.csv')


# In[19]:


schema_df.head(10)


# In[7]:





# In[11]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[12]:


schema_df


# In[6]:


df


# In[21]:


df.columns


# In[11]:


df.iloc[0] #integer location -you can pass a list of raws and cols -ex. df.iloc[[0,1], [0]]


# In[24]:


df.loc[0, 'Respondent'] #here I can use labels


# In[25]:


df.shape


# In[26]:


df['Respondent']


# In[29]:


df['Hobbyist'].value_counts() #it counts how many of all possible answers


# In[34]:


df.loc[0:3, 'Hobbyist':'Employment'] #it slices the raws from 0 to 3, col from 'Hobbyist' to 'Employment'


# In[42]:


df.set_index('Employment')


# In[40]:


schema_df.sort_index(ascending=False)


# In[51]:


filt = (df['Employment'] == 'Employed full-time') & (df['Country'] == 'Italy')


# In[52]:


df.loc[filt] #negation of filter is given by: df.loc[~filt]


# In[76]:


female = (df['Gender'] == 'Woman') & (df['ConvertedComp'] > 70000) & (df['Country'] != 'United States') 


# In[77]:


df.loc[female, ['Country', 'ConvertedComp']]


# In[82]:


countries = ('Italy', 'Canada')
filt_2 = df['Country'].isin(countries)


# In[83]:


df.loc[filt_2]


# In[85]:


df.columns


# In[95]:


filt_3 = df['LanguageWorkedWith'].str.contains('Python', na=False)


# In[97]:


df.loc[filt_3]


# In[ ]:




