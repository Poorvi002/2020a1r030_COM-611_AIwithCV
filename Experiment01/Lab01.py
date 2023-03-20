#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Implement and demostrate the date processing for finding the most specific hypothesis 
based on a given set of training data samples"""
import csv
numm=3
a=[]
print("\n The given training data set \n")
with open("C:/Users/HP/Desktop/A1R030_01.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)
print("\n The initial values of hypothesis \n")
hypothesis=['0']*numm
print(hypothesis)

for j in range(0,numm):
    hypothesis[j]= a[0][j]
print("\n Find S: Finding a maximally specific hypothesis \n")
for i in range(0,len(a)):
    if a[i][numm]=="positive":
        for j in range(0,numm):
            if a[i][j]!= hypothesis[j]:
                hypothesis[j]='?'
            else:
                hypothesis[j]=a[i][j]
    print("For training instance no:{0} the hypothesis is".format(i),hypothesis)
print("\n The maximally specific hypothesis for a given training example: \n")
print(hypothesis)


# In[ ]:




