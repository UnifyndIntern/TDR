# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:55:14 2017

@author: Dhaval
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:31:39 2017

@author: dhaval
"""
# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run(a,b):
    print(a,b)
    for x in range(a,b):
        r_TD2013(x)
        r_TD2014(x)
        r_TD2015(x)
        r_TD2016(x)
        r_TD2017(x)
        s_TD2013(x)
        s_TD2014(x)
        s_TD2015(x)
        s_TD2016(x)
        s_TD2017(x)

# Plotting Graphs
def rent_plot(loc):
    plt.figure(figsize = (100,20))
    sns.pointplot(x = r_columns, y = df_td.iloc[loc, 57:109])

def sales_plot(loc):
    plt.figure(figsize = (100,20))
    sns.pointplot(x = s_columns, y = df_td.iloc[loc, 5:57])

def td_plot(loc):
    plt.figure(figsize = (100,20))
    sns.pointplot(x = td_columns, y = df_td.iloc[loc, 109:161]) 

def r_TD2013(loc):
    # Year 2013(Sales and TD)
    fig = plt.figure(figsize=(25,15))
    plt.ioff()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    a1 = sns.pointplot(x = r_2013, y = df_td.iloc[loc, 58:67], ax= ax1)
    a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
    a2 = sns.pointplot(x = td_2013, y = df_td.iloc[loc, 110:119], ax = ax2)
    a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
    fig.savefig('Results/'+str(brand[loc])+'/r_TD2013.png')
    plt.close()

def r_TD2014(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2014, y = df_td.iloc[loc, 67:79], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2014, y = df_td.iloc[loc, 119:131], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/r_TD2014.png')
	plt.close()


def r_TD2015(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()

	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2015, y = df_td.iloc[loc, 79:91], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2015, y = df_td.iloc[loc, 131:143], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/r_TD2015.png')
	plt.close()

def r_TD2016(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2016, y = df_td.iloc[loc, 91:103], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2016, y = df_td.iloc[loc, 143:155], ax = ax2)
	a2.set(xticklabels = [], ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/r_TD2016.png')
	plt.close()

def r_TD2017(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2017, y = df_td.iloc[loc, 103:110], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2017, y = df_td.iloc[loc, 155:162], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/r_TD2017.png')
	plt.close()
    
def s_TD2013(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2013, y = df_td.iloc[loc, 6:15], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2013, y = df_td.iloc[loc, 110:119], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/s_TD2013.png')
	plt.close()

def s_TD2014(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2014, y = df_td.iloc[loc, 15:27], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2014, y = df_td.iloc[loc, 119:131], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/s_TD2014.png')
	plt.close()

def s_TD2015(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2015, y = df_td.iloc[loc, 27:39], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2015, y = df_td.iloc[loc, 131:143], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/s_TD2015.png')
	plt.close()

def s_TD2016(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2016, y = df_td.iloc[loc, 39:51], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2016, y = df_td.iloc[loc, 143:155], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/s_TD2016.png')
	plt.close()

def s_TD2017(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2017, y = df_td.iloc[loc, 51:58], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2017, y = df_td.iloc[loc, 155:162], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/s_TD2017.png')
	plt.close()

# Plotting for Category, Format and Floor
def plot(x,y,hue):
    x = str(x)
    y = str(y)
    hue = str(hue)
    
    plt.figure(figsize=(26,14))
    plt.title(""+x+" analysis for "+y[0:8])
    plt.ioff()
    sns.barplot(x = df_td[x], y = df_td[y], hue = df_td[hue],ci = None)
    plt.savefig(""+x+"/"+x+"wise wrt "+hue+" "+y[0:8]+".png")
    plt.close()
      
# Importing the data 
df_td = pd.read_excel('TD.xlsx')

# Renaming Category - New Format
from sklearn.preprocessing import LabelEncoder
category_labelencoder = LabelEncoder()
df_td['Category - New format'] = category_labelencoder.fit_transform(df_td['Category - New format'])
category_decode = category_labelencoder.inverse_transform(df_td['Category - New format'])

# Renaming Format
format_labelencoder = LabelEncoder()
df_td['Format'] = format_labelencoder.fit_transform(df_td['Format'].fillna('0'))
format_decode = format_labelencoder.inverse_transform(df_td['Format'])


df_td_columns = list(df_td.columns)
s_columns = df_td_columns[6:58]
r_columns = df_td_columns[58:110]
td_columns = df_td_columns[110:162]

df_td['Avg 2013 \nTD'] = df_td.iloc[:,110:119].mean(axis = 1)
df_td['Avg 2014 \nTD'] = df_td.iloc[:,119:131].mean(axis = 1)
df_td['Avg 2015 \nTD'] = df_td.iloc[:,131:143].mean(axis = 1)
df_td['Avg 2016 \nTD'] = df_td.iloc[:,143:155].mean(axis = 1)
df_td['Avg 2017 \nTD'] = df_td.iloc[:,155:162].mean(axis = 1)

analysis_td = df_td_columns[110:167]
avg_analysis_td = df_td_columns[162:167]
df_td_columns = list(df_td.columns)

# Sales Per Year
s_2013 = s_columns[0:9]
s_2014 = s_columns[9:21]
s_2015 = s_columns[21:33]
s_2016 = s_columns[33:45]
s_2017 = s_columns[45:52]
s_years = [s_2013, s_2014, s_2015, s_2016, s_2017]

# Rent Per Year
r_2013 = r_columns[0:9]
r_2014 = r_columns[9:21]
r_2015 = r_columns[21:33]
r_2016 = r_columns[33:45]
r_2017 = r_columns[45:52]
r_years = [r_2013, r_2014, r_2015, r_2016, r_2017]

# Rent Per Year
td_2013 = td_columns[0:9]
td_2014 = td_columns[9:21]
td_2015 = td_columns[21:33]
td_2016 = td_columns[33:45]
td_2017 = td_columns[45:52]
td_years = [td_2013, td_2014, td_2015, td_2016, td_2017] 


years = ['2013', '2014', '2015', '2016', '2017']

# Creating list for all Brands
brand_dir = []
brand = []
for i in df_td['Brand Name']:
    brand_dir.append("\'"+str(i)+"\'")
    brand.append(str(i))
brand.pop(220)
brand_dir.pop(220)
brand.insert(220,'Omega Cartier')
brand_dir.insert(220,"'Omega Cartier'")

# Category dataframe
category = pd.DataFrame(data = df_td, columns = ['Brand Name', 'Category - New format', 'Avg 2013 \nTD', 'Avg 2014 \nTD', 'Avg 2015 \nTD', 'Avg 2016 \nTD', 'Avg 2017 \nTD'])



















"""

# Creating Folders for saving brandwise performance
import os
os.mkdir("Results")
for x in brand:
    os.mkdir("Results/"+str(x))
"""
# Creating folders for saving Category, Format and Floorwise performance
import os
os.mkdir("Category - New format")
os.mkdir("Format")
os.mkdir("Floor")
"""
# os.mkdir solves the problem, no need to perform this
# Creating Folders for Claire's and Jonah's
os.mkdir('Results/Claire\'s')
os.mkdir('Results/Jonah\'s')
for y in years:
    os.mkdir('Results/Claire\'s/'+y)
    os.mkdir('Results/Jonah\'s/'+y)

# Saving graphs for every brand by Rent vs TD and Sales vs TD
run(0,len(brand))
"""
analysis = ['Floor', 'Format', 'Category - New format']

for y in avg_analysis_td: 
    plot('Floor',y,'Format')
    plot('Floor',y,'Category - New format')
    plot('Format',y,'Floor')
    plot('Format',y,'Category - New format')
    plot('Category - New format',y,'Floor')
    plot('Category - New format',y,'Format')
plot('Category - New format', 'Avg 2013 \nTD', 'Format')
    
r_TD2013(2)
r_TD2014(2)
r_TD2015(2)
r_TD2016(2)
r_TD2017(2)
s_TD2013(2)
s_TD2014(2)
s_TD2015(2)
s_TD2016(2)
s_TD2017(2)"""