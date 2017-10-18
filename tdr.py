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

def total_avg(x, name):
    df['Total Avg '+name] = df[x[:]].mean(axis = 1)

def count(df):
    count = df.index.value_counts().to_frame()
    count.reset_index(inplace = True)
    count.columns = ['Column', 'Counts']
    count['Divide'] = count['Counts'] // 5
    count['Extra'] = count['Counts'] % 5
    return count

def pivot(df, values, column):
    """
    df :
        Data Type: Data Frame
        
        Dataframe to be pivoted
    values : 
        Data Type: String (To be written inside Double Single quotes)
        
        Value according to which the table will be pivoted
    column : 
        Data Type: String (To be written inside Double Single quotes)
        
        To set Category/Floor as the column
    
    Example:
        pivot = pivot(floor_2014, 'Avg 2014 TD', 'Floor')
    """
    df = df[df[values].notnull()]
    pivot = df.pivot_table(values = values, index = [column, 'Brand Name'])
    pivot = pivot.reset_index().sort_values([column, values]).set_index([column])
    return pivot

def multiple(count, pivot_df):
    pivot_df['Multiple'] = np.nan
    multiple = [5, 4, 3, 2, 1, 1]
    length = len(count)
    i = 0
    for i in range(0,length):
        x = 0
        y = count['Divide'][i]
        a = 0
        while((y <= count['Counts'][i]) & (a < 6)):
            print(i,a,x,y)
            pivot_df.ix[count['Column'][i]]['Multiple'][x:y] = multiple[a]
            x = y
            a = a + 1
            if y > count['Counts'][i]:
                y = y + count['Extra'][i]
            else:
                y = y + count['Divide'][i]
    pivot_df['Multiple'] = pivot_df['Multiple'].replace(np.nan, 1) 
    return pivot_df

# Importing the libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing data
df_temp = pd.read_excel('Master Sales Data July 2017.xlsx')
df_temp = df_temp.iloc[:327,:]

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

# Calculating Total Avg for Sales, Rent and TDR
total_avg(sales, 'Sales')
total_avg(rent, 'Rent')
total_avg(td, 'TD')

# Floor DataFrame
final_df = pd.DataFrame(data = df, columns = ['Brand Name', 'Floor', 'Category - New format', 'Avg 2013 TD', 'Avg 2014 TD', 'Avg 2015 TD', 'Avg 2016 TD', 'Avg 2017 TD'])
floor_2013 = pivot(final_df, 'Avg 2013 TD', 'Floor')
count_2013 = count(floor_2013)
a = multiple(count_2013,floor_2013)
"""
cat_2013 = pivot(final_df, 'Avg 2013 TD', 'Category - New format')
floor_2013 = pd.DataFrame()
floor_2013 = floor[floor['Avg 2013 TD'].notnull()]
floor_2013 = floor_2013.iloc[:,0:3]
floor_2013['Decision'] = floor_2013['Avg 2013 TD'] > 20


floor_2014 = pd.DataFrame()
floor_2014 = floor[floor['Avg 2014 TD'].notnull()]
floor_2014 = floor_2014[['Brand Name', 'Floor', 'Avg 2014 TD']]

floor_2015 = pd.DataFrame()
floor_2015 = floor[floor['Avg 2015 TD'].notnull()]
floor_2015 = floor_2015[['Brand Name', 'Floor', 'Avg 2015 TD']]

floor_2016 = pd.DataFrame()
floor_2016 = floor[floor['Avg 2016 TD'].notnull()]
floor_2016 = floor_2016[['Brand Name', 'Floor', 'Avg 2016 TD']]

floor_2017 = pd.DataFrame()
floor_2017 = floor[floor['Avg 2017 TD'].notnull()]
floor_2017 = floor_2017[['Brand Name', 'Floor', 'Avg 2017 TD']]

pivot = floor_2013.pivot_table(values = 'Avg 2013 TD', index = ['Floor', 'Brand Name'])

sort_pivot = pivot.reset_index().sort_values(['Floor','Avg 2013 TD'])

pivot_2014 = pivot(floor_2014, 'Avg 2014 TD', 'Floor')

count_2013 = count(cat_2013)
count_2014 = count(floor_2014, 'Floor')

sort_pivot['Multiple'] = np.nan
sort_pivot.ix[count_2013['Column'][0]]['Multiple'][0:13] = 1
"""
