# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:15:42 2017

@author: Dhaval
"""
def avg(x, name):
    df['Avg 2013 '+name] = df[x[0:12]].mean(axis = 1)
    df['Avg 2014 '+name] = df[x[12:24]].mean(axis = 1)
    df['Avg 2015 '+name] = df[x[24:36]].mean(axis = 1)
    df['Avg 2016 '+name] = df[x[36:48]].mean(axis = 1)
    df['Avg 2017 '+name] = df[x[48:52]].mean(axis = 1)

# Importing the libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing data
df_temp = pd.read_excel('Master Sales Data July 2017.xlsx')

# Delete Unnecessary Columns in Data
df = df_temp.drop(['Sr. No.'], axis = 1)
df.drop(['Yardi - Lease Details'], axis = 1, inplace = True)
df.drop(['Lease Code'], axis = 1, inplace = True)
df.drop(['Unit Nos'], axis = 1, inplace = True)
df.drop(['Trading Date'], axis = 1, inplace = True)
df.drop(['Term Expiry Date'], axis = 1, inplace = True)
df.drop(df.iloc[:,114:273], axis = 1, inplace = True)
df.drop(df.iloc[:,166:169], axis = 1, inplace = True)
df.drop(['YTD \nAvg Sales\n2017-18'], axis = 1, inplace = True)

# Label encoding
# Renaming Category - New Format
from sklearn.preprocessing import LabelEncoder
category_labelencoder = LabelEncoder()
df['Category - New format'] = category_labelencoder.fit_transform(df['Category - New format'].fillna('0'))

# Renaming Format
format_labelencoder = LabelEncoder()
df['Format'] = format_labelencoder.fit_transform(df['Format'].fillna('0'))

# Renaming Floor
floor_labelencoder = LabelEncoder()
df['Floor'] = floor_labelencoder.fit_transform(df['Floor'].fillna('0'))

# Renaming Source
source_labelencoder = LabelEncoder()
df['Source'] = source_labelencoder.fit_transform(df['Source'].fillna('0'))

# Renaming MG/PRS
mg_labelencoder = LabelEncoder()
df['MG/PRS'] = mg_labelencoder.fit_transform(df['MG/PRS'].fillna('0'))

# Columns of TD
columns = list(df.columns)

# Imp elements
sales = columns[9:61]
rent = columns[113:165]
td = columns[61:113]

# TDR calculation
# Replacing 0 With NaN to avoid 'Divide By Zero Error'    
df[sales[:]] = df[sales[:]].replace({0:np.nan})
df[rent[:]] = df[rent[:]].replace({0:np.nan})
df[td[:]] = df[td[:]].replace({0:np.nan})

for x in range(0,52):
    df[td[x]] = df[td[x]] / df[rent[x]]
    
# Calculating Avg for Sales, Rent and TDR
avg(sales,'Sales')
avg(rent,'Rent')
avg(td,'TD')