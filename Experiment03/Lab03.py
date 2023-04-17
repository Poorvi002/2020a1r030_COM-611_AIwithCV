#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pylab as plt


# In[3]:


filename = "C:/Users/HP/Desktop/python.py/auto.csv"


# In[4]:


headers = ["symboling","normalized-losses","make","fule-type","aspiration","num-of-doors","body-style",
          "drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type",
          "num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
          "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv(filename,names = headers)
df.head()

import numpy as np
df.replace("?",np.nan, inplace = True)
df.head()

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")



# In[5]:


#calculate the mean value for the "normalized-losses" column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("average of normalized-losses:",avg_norm_loss)


# In[6]:


#replace "NaN" with mean value in "normalized_losses" colmun
df["normalized-losses"].replace(np.NaN, avg_norm_loss, inplace = True)
df.head()


# In[7]:


#calculate the mean value for the "bore" column
avg_bore = df["bore"].astype("float").mean(axis=0)
print("average of bore:",avg_bore)


# In[8]:


#Replace "nan" with the mean value in the "bore" column
df["bore"].replace(np.NaN, avg_bore, inplace = True)
df.head()


# In[9]:


#calculate the mean value for the "horsepower" column
avg_horsepower = df["horsepower"].astype("float").mean(axis=0)
print("average of horsepower:",avg_horsepower)
#Replace "nan" with the mean value in the "horsepower" column
df["horsepower"].replace(np.NaN, avg_horsepower, inplace = True)
df.head()


# In[10]:


#calculate the mean value for the "peak-rpm" column
avg_peak_rpm = df["peak-rpm"].astype("float").mean(axis=0)
print("average of peak-rpm:",avg_peak_rpm)
#Replace "nan" with the mean value in the "peak-rpm" column
df["peak-rpm"].replace(np.NaN, avg_peak_rpm, inplace = True)
df.head()


# In[11]:


#calculate the mean value for the "stroke" column
avg_stroke = df["stroke"].astype("float").mean(axis=0)
print("average of stroke:",avg_stroke)
#Replace "nan" with the mean value in the "stroke" column
df["stroke"].replace(np.NaN, avg_stroke, inplace = True)
df.head()


# In[12]:


#calculate the mean value for the "price" column
avg_price = df["price"].astype("float").mean(axis=0)
print("average of price:",avg_price)
#Replace "nan" with the mean value in the "price" column
df["price"].replace(np.NaN, avg_price, inplace = True)
df.head()


# In[13]:


df['num-of-doors'].value_counts


# In[14]:


df['num-of-doors'].value_counts().idxmax()


# In[15]:


#replace the missing 'num-of-doors' values by the most frequent
df["num-of-doors"].replace(np.nan, "four", inplace=True)


# In[16]:


df.head(40)


# In[17]:


#simply drop whole row with NaN in "price" column
df.dropna(subset=["price"],axis=0, inplace=True)

#reset index, because we dropped two rows
df.reset_index(drop=True, inplace=True)


# In[18]:


df.head()


# In[19]:


df.dtypes


# In[20]:


df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("float")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")


# In[21]:


df.dtypes


# In[22]:


#data standardization
#subtracting the mean and divide by standard deviation
df.head()


# In[23]:


#covert mpg to l/100km by mathematical operation (235 divided by mpg)
df['city-l/100km']= 235/df["city-mpg"]
df.head()


# In[24]:


df["highway-mpg"]=235/df["highway-mpg"]
df.rename(columns={"highway-mpg":'hghwat-l/100km'},inplace=True)
df.head()


# In[25]:


#replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


# In[26]:


df['height'] = df['height']/df['height'].max()
df[["length", "width", "height"]].head()


# In[27]:


#binning
df["horsepower"] = df["horsepower"].astype(int, copy=True)


# In[28]:


import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"])

#set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# In[29]:


bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins


# In[30]:


group_names = ['low', 'medium', 'high']


# In[31]:


df['horsepower-binned']=pd.cut(df['horsepower'], bins, labels = group_names, include_lowest=True)
df[['horsepower','horsepower-binned']].head(20)


# In[32]:


df["horsepower-binned"].value_counts()


# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, df["horsepower-binned"].value_counts())

#set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# In[34]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot

#draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"],bins = 3)

#set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# In[35]:


#indicator variable
df.columns


# In[36]:


dummy_variable_1 = pd.get_dummies(df["fule-type"])
dummy_variable_1.head()


# In[37]:


#change the column names for clarity
dummy_variable_1.rename(columns={'gas':'fuel-type-gas','diesel':'fuel-type-diesel'},inplace=True)
dummy_variable_1.head()


# In[38]:


#merge data  frame "df" and "dummy_variable_1"
df = pd.concat([df, dummy_variable_1], axis=1)

#drop original column "fuel-type" from "df"
df.drop("fule-type", axis = 1, inplace = True)
df.head()


# In[39]:


dummy_variable_2 = pd.get_dummies(df["aspiration"])
dummy_variable_2.rename(columns={'std':'aspiration-std', 'turbo': 'aspiration-turbo'},inplace=True)
dummy_variable_2.head()


# In[40]:


#merge the new dataframe to the original dataframe
df = pd.concat([df, dummy_variable_2], axis = 1)

#drop original column "fuel-type" from "df"
df.drop("aspiration", axis = 1,inplace = True)
dummy_variable_2.head()


# In[41]:


df.head()


# In[44]:


df.to_csv("C:/Users/HP/Desktop/python.py/clean_df.csv")


# In[ ]:




