# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:24:31 2018

@author: Anjali Brajendra
"""

import pandas as pd
import matplotlib.pyplot as plt


#print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])


df1 = pd.read_csv("E:\Brajendra\Python\Python-Data\Vechiles-data.txt",skiprows=[0],
                  names=['ROW1','DLR_NO','RO_NO','WORK_TYPE','VIN'])
print(df1)
df1 = df1.drop('ROW1', axis=1)
df = pd.DataFrame(df1)
df = df.head(100)
#result = df.set_index('VIN').to_dict()
#print(result)

#covert to series
#1 set of data
dfSet1 = df.groupby(['VIN','DLR_NO','RO_NO','WORK_TYPE'])['RO_NO'].count()
dfSet1.to_csv("E:\Brajendra\Python\Python-Data\Set1.txt")
#print(dfSet1)

#2 set of data
dfSet2 = df.groupby(['VIN','DLR_NO'])['VIN'].count()
dfSet2.to_csv("E:\Brajendra\Python\Python-Data\Set2.txt")
#print(dfSet2)

#3 set of data
dfSet3 = df.groupby(['VIN'])['VIN'].count()
dfSet3.to_csv("E:\Brajendra\Python\Python-Data\Set3.txt")
#print(dfSet3)

#graph Frequency Count
dfSet3 = pd.read_csv("E:\Brajendra\Python\Python-Data\Set3.txt",
                     names=['VIN','count'])
dfSet3=dfSet3.head(20)
plt.xticks(rotation=90)
plt.bar(dfSet3['VIN'].tolist(), dfSet3['count'].tolist(), 1/2.2, color="blue")
plt.show()




