# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:56:46 2021

@author: Grace
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('NBA_mvp.csv') 
print (data.describe())
""" show data"""

print(data['Age'].max())   
print(data[data.Age==data.Age.max()])
"""show the oldest plyaer when they win the MVP"""

mvp_age30=data.loc[data.Age>=30][['Player','Age']]
print(mvp_age30)
""" MVP over the age of 30 """

print(data.Player.value_counts())
""" Player with the most MVPs """

avg=pd.Series({'point':data.PTS.mean(),
              'rebounds':data.TRB.mean(),
              'assistants':data.AST.mean(),
              'steals':data.STL.mean(),
              'block':data.BLK.mean()})
""" The avergae performance of the MVPs."""

print(avg)
avg.plot(kind='bar',
         yticks=[x for x in range(1,30,2)],
         color='g',rot=-45,
         title='MVPs')

corrmat = data.corr()
f,ax = plt.subplots(figsize=(12,6))
sns.heatmap(corrmat,annot=True)