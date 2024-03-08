#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[34]:


data = pd.read_csv('cleaned_headlines.csv')


# In[35]:


data.shape


# In[36]:


test_data = data[0:500]


# In[37]:


test_data.head()


# In[38]:


nans_df =test_data[test_data['Manual Sentiment'].isna()]
nans_df


# In[31]:


data.loc[228, 'Manual Sentiment'] = -1


# In[32]:


nans_df =test_data[test_data['Manual Sentiment'].isna()]
nans_df


# In[8]:


data.to_csv('cleaned_headlines.csv', index=False)


# In[9]:


cleaned_headlines.csv


# ## Cleaning Source from Headlines
# 

# In[12]:


data = pd.read_csv('labeled_headlines.csv')


# In[13]:


data


# In[17]:


news_headline = "Iran uses Artificial Intelligence for maximizing suppression: Experts - ANI News"
def strip_source(news_headline):
    # Reverse the string
    reversed_headline = news_headline[::-1]
    
    # Find the index of the first dash in the reversed string
    index_of_dash = reversed_headline.find('-')
    
    if index_of_dash != -1:
        # Remove everything up to the first dash
        modified_headline = reversed_headline[index_of_dash+1:].strip()
    else:
        # If dash not found, return the original reversed headline
        modified_headline = reversed_headline
    
    # Reverse the modified string back to the original order
    modified_headline = modified_headline[::-1]

    return modified_headline


# In[18]:


data['cleaned_title'] = data['translated_title'].apply(strip_source)


# In[21]:


data['translated_title'].head()


# In[22]:


data.to_csv('clean_titles.csv', index = False)


# In[ ]:




