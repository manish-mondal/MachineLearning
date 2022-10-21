#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:
arr = []
for i in range(15):
    arr.append(random.randint(1,20))
ans = np.array(arr)


# In[3]:
ans


# In[4]:
reshaped = np.reshape(ans,(3,5))
reshaped


# In[5]:
reshaped.shape


# In[6]:
for x in reshaped:
    maxx = max(x)
    for i in range(x.shape[0]):
        if x[i] == maxx:
            x[i]=0
reshaped

# In[7]:
import pandas as pd


# In[8]:
df = pd.read_csv(r"C:\Users\mondal\Documents\documents_ucmo\ucm university\Machine learning\Assignment 2\data.csv")


# In[ ]:





# In[9]:
df.describe()


# In[10]:
df.fillna(df.mean(),inplace=True)


# In[11]:
df.iloc[17]


# In[12]:
df.groupby(['Duration','Pulse']).mean()
df.groupby(['Duration','Pulse']).max()
df.groupby(['Duration','Pulse']).count()
df.groupby(['Duration','Pulse']).min()


# In[13]:
df[(df['Calories']>=500) & (df['Calories']<=1000)]


# In[14]:


df[(df['Calories']>500) & (df['Pulse']<100)]


# In[15]:
df_modified = df[["Duration","Pulse","Calories"]].copy()
df_modified


# In[16]:
df.drop(['Maxpulse'],axis=1)


# In[17]:


df["Calories"] = df["Calories"].astype(int)
df["Calories"].dtype


# In[18]:
df.plot.scatter(x = 'Duration', y = 'Calories')


# In[19]:
import matplotlib.pyplot as plt
import numpy as np

y = np.array([ 22.2, 17.6, 8.8, 8, 7.7, 6.7])
mylabels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
myexplode = [0.2, 0, 0, 0,0,0]
plt.pie(y, labels = mylabels,explode = myexplode,autopct='%1.1f%%',startangle = 130)
plt.show() 


# In[ ]:




