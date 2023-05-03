#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""implement the KNN IRIS image. classification based on a given set of training data sample.
read the training data from a .csv file."""


# In[4]:


#importing the libraraies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split


# In[5]:


#read the data set
iris=pd.read_csv('C:/Users/student/Downloads/iris.csv')
iris.tail()


# In[6]:


#data visualization
iris.shape


# In[7]:


iris['Species'].value_counts()


# In[8]:


iris.columns


# In[9]:


iris.values


# In[10]:


iris.info()


# In[11]:


iris.describe(include='all')


# In[12]:


x=iris.iloc[:,:4]
x.head()


# In[13]:


y=iris.iloc[:,-1]
y.head()


# In[15]:


#data normalization
x=preprocessing.StandardScaler().fit_transform(x)
x[0:4]


# In[17]:


#train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3, random_state=1)
y_test.shape


# In[18]:


#training and predicting
knnmodel = KNeighborsClassifier(n_neighbors=3)


# In[19]:


knnmodel.fit(x_train,y_train)


# In[20]:


y_predict1=knnmodel.predict(x_test)


# In[21]:


#accuracy
from sklearn.metrics import accuracy_score


# In[22]:


acc=accuracy_score(y_test,y_predict1)
acc


# In[23]:


#confusion matrix
from sklearn.metrics import confusion_matrix
cn=confusion_matrix(y_test.values,y_predict1)
cn


# In[24]:


cn1=pd.DataFrame(data=cn,index=['setosa','versicolor','virginica'],columns=['setosa','versicolor','virginica'])
cn1


# In[27]:


#output visualization
prediction_output=pd.DataFrame(data=[y_test.values, y_predict1],index=['y_test','y_predict1'])


# In[28]:


prediction_output.transpose()


# In[29]:


prediction_output.iloc[0,:].value_counts()


# In[32]:


#finding the vsalue of k
ks=50
mean_acc=np.zeros((ks-1))

#train and predict
for n in range(1,ks):
    neigh=KNeighborsClassifier(n_neighbors=n).fit(x_train,y_train)
    yhat=neigh.predict(x_test)
    mean_acc[n-1]=accuracy_score(y_test,yhat)


# In[33]:


print(mean_acc)


# In[34]:


print("the best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1)


# In[35]:


plt.plot(range(1,ks),mean_acc,'g')
plt.legend(('accuracy'))
plt.ylabel('acccuracy')
plt.xlabel('number of neighbors(k)')
plt.tight_layout()
plt.show()


# In[ ]:




