# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:20:32 2017

@author: Balaji
"""

import pandas as pd
import numpy as np 
path='data1.csv'
df=pd.read_csv(path, index_col=False, parse_dates=True)
df1=pd.DataFrame(df)
#df.fillna(df.mode().iloc[0])
#print(df.iloc[0])
x=np.array(df.columns)
#print(x)
rowsno=df[x[0]].count()
for col in df.columns:
        m=df[col].mode()
        dtp=df[col].dtype
        if(df[col].dtype==np.float64):
            df[col].fillna(value = float(m), inplace=True)     
df.to_csv('d9.csv')    
    