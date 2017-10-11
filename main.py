#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:31:39 2017

@author: dhaval
"""
# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def run(a,b):
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
    
    a1 = sns.pointplot(x = r_2013, y = df_td.iloc[loc, 57:66], ax= ax1)
    a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
    a2 = sns.pointplot(x = td_2013, y = df_td.iloc[loc, 109:118], ax = ax2)
    a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
    fig.savefig('Results/'+str(brand[loc])+'/2013/r_TD2013.png')
    plt.close()

def r_TD2014(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2014, y = df_td.iloc[loc, 66:78], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2014, y = df_td.iloc[loc, 118:130], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2014/r_TD2014.png')
	plt.close()


def r_TD2015(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()

	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2015, y = df_td.iloc[loc, 78:90], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2015, y = df_td.iloc[loc, 130:142], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2015/r_TD2015.png')
	plt.close()

def r_TD2016(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2016, y = df_td.iloc[loc, 90:102], ax= ax1)
	a1.set(ylabel = 'Rent', title = 'Rent for Different Months')
	a2 = sns.pointplot(x = td_2016, y = df_td.iloc[loc, 142:154], ax = ax2)
	a2.set(xticklabels = [], ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2016/r_TD2016.png')
	plt.close()

def r_TD2017(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = r_2017, y = df_td.iloc[loc, 102:109], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2017, y = df_td.iloc[loc, 154:161], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2017/r_TD2017.png')
	plt.close()
    
def s_TD2013(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2013, y = df_td.iloc[loc, 5:14], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2013, y = df_td.iloc[loc, 109:118], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2013/s_TD2013.png')
	plt.close()

def s_TD2014(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2014, y = df_td.iloc[loc, 14:26], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2014, y = df_td.iloc[loc, 118:130], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2014/s_TD2014.png')
	plt.close()

def s_TD2015(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2015, y = df_td.iloc[loc, 26:38], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2015, y = df_td.iloc[loc, 130:142], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2015/s_TD2015.png')
	plt.close()

def s_TD2016(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2016, y = df_td.iloc[loc, 38:50], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2016, y = df_td.iloc[loc, 142:154], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2016/s_TD2016.png')
	plt.close()

def s_TD2017(loc):
	# Year 2013(Sales and TD)
	fig = plt.figure(figsize=(25,15))
	plt.ioff()
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	a1 = sns.pointplot(x = s_2017, y = df_td.iloc[loc, 50:57], ax= ax1)
	a1.set(ylabel = 'Sales', title = 'Sales for Different Months')
	a2 = sns.pointplot(x = td_2017, y = df_td.iloc[loc, 154:161], ax = ax2)
	a2.set(ylabel = 'Trading Density', title = 'Trading Density for Different Months')
	fig.savefig('Results/'+str(brand[loc])+'/2017/s_TD2017.png')
	plt.close()

# Importing data
df = pd.read_excel('Master Sales Data July 2017.xlsx')

# Delete Unnecessary Columns in Data
cleaned_data = df.drop(['Sr. No.'], axis = 1)
cleaned_data.drop(['Yardi - Lease Details'], axis = 1, inplace = True)
cleaned_data.drop(['Lease Code'], axis = 1, inplace = True)

# List of columns of Old TD and rent
cleaned_data_columns = list(cleaned_data.columns)
s_columns = cleaned_data_columns[12:64]
r_columns = cleaned_data_columns[276:328]
td_columns = cleaned_data_columns[65:117]

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

# Replacing 0 With NaN to avoid 'Divide By Zero Error'    
cleaned_data[s_columns[:]] = cleaned_data[s_columns[:]].replace({0:np.nan})
cleaned_data[r_columns[:]] = cleaned_data[r_columns[:]].replace({0:np.nan})
cleaned_data[td_columns[:]] = cleaned_data[td_columns[:]].replace({0:np.nan})

# TD Calculation
for x in range(0,52):
    cleaned_data[td_columns[x]] = cleaned_data[td_columns[x]] / cleaned_data[r_columns[x]]

# New Data Frame for TD analysis
columns = list(cleaned_data.columns)
column_td = ['Brand Name', 'Floor', 'Format', 'Category - New format', 'Carpet Area']

# Added all columns of Sales to column list
for x in range(0,52):
    column_td.append(s_columns[x])
# Added all columns of Rent to column list
for x in range(0,52):
    column_td.append(r_columns[x])
# Added all columns of TD to column list
for x in range(0,52):
    column_td.append(td_columns[x])

df_td = pd.DataFrame(data = cleaned_data, columns = column_td)
df_td = df_td.iloc[0:327,:] # Selected 327 rows as the remaining were blank

df_td.sort_values(['Brand Name'])

# Creating Folders for all Brands
brand_dir = []
brand = []
for i in df_td['Brand Name']:
    brand_dir.append("\'"+str(i)+"\'")
    brand.append(str(i))
brand.sort()
brand_dir.sort()
brand.pop(221)
brand_dir.pop(221)
brand_dir.append("'Omega Cartier'")
brand.append('Omega Cartier')
brand.sort()
brand_dir.sort()


import os
os.system("mkdir Results")
for x in brand_dir:
    os.system("mkdir Results/"+str(x))
    os.system("cd Results/"+str(x))
    for y in years:
        os.system("mkdir Results/"+str(x)+"/"+y)

# Creating Folders for Claire's and Jonah's
os.mkdir('Results/Claire\'s')
os.mkdir('Results/Jonah\'s')
for y in years:
    os.mkdir('Results/Claire\'s/'+y)
    os.mkdir('Results/Jonah\'s/'+y)



for x in range(0,6):
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

