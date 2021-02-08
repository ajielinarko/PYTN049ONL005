# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:44:35 2020

@author: user
"""

##Training Python Sesi 7: Basic Visualization

import numpy as np
import pandas as pd

#membuka data excel
#url = 'C:\tes\python\data-contoh\Canada-data-contoh-sesi7.xlsx'
df_can = pd.read_excel(r'C:\tes\python\data-contoh\Canada-data-contoh-sesi7.xlsx',
                       sheet_name = 'Canada by Citizenship',
                       skiprows = range(20),
                       skipfooter = 2)
print('Data read into a pandas dataframe')
df_can.head()
df_can.tail()
df_can.info()

#untuk mendapatkan list header kolom
df_can.columns.values

#melihat daftar index
df_can.index.values

#melihat informasi data frame
df_can.shape  

#untuk membersihkan dataset dengan menghapus bbrp kolom yg tidak perlu
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)

#untuk mengganti nama kolom
df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent',
                       'RegName': 'Region'}, inplace=True)
df_can.columns

#menambahkan kolom "Total" yg merangkum total imigran menurut negara selama periode 1980-2013
df_can['Total'] = df_can.sum(axis=1)
df_can.columns

#untuk memeriksa berapa banyak objek null dalam suatu dataset
df_can.isnull().sum()

#untuk melihat ringkasan singkat dari setiap kolom
df_can.describe()


## Pandas: Indexing and Selection (Slicing)

#SELECT COLUMN
#select column with filter
df_can.Country

#filter daftar negara dan data selama tahun 1980-1985
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]

#SELECT ROW
#menyetel kolom 'Country" sebagai indeks
df_can.set_index('Country', inplace=True)
df_can.head(3)

#untuk me-remove nama indeks
#df_can.index.name=None

#untuk melihat jumlah imigran dari Jepang dengan berbagai skenario
# 1. Full row data (all columns)
print(df_can.loc['Japan'])

# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
print(df_can.loc['Japan', 2013])

#alternate methods
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1985]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

#untuk mengubah nama kolom menjadi string, untuk menghindari ambiguitas antara nama kolom 'angka' dan indeks 'angka'
df_can.columns = list (map(str, df_can.columns))

#krn kita telah mendeklarasikan tahun sebagai "string" pd langkah diatas,
#skrg kita perlu mendeklarasikan variabel agar mudah dipanggil rentang tahun secara penuh
years = list(map(str, range(1980, 2014)))
years

#Filtering based criteria

# 1. create condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

# 2. pass this condition into the dataframe
df_can[condition]

#filter for AreaName = Asia and RegName = Southern Asia
df_can[(df_can['Continent'] == 'Asia') & (df_can['Region'] == 'Southern Asia')]

#untuk meninjau perubahan yg telah kita lakukan
print('Data dimension:', df_can.shape)
print(df_can.columns)
df_can.head(2)


##VISUALIZING DATA USING MATPLOTLIB
#Matplotlib: pyplot
%matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt

#to know matplotlib version
print('Matplotlib version: ', mpl.__version__)

print(plt.style.available)
mpl.style.use(['ggplot'])
haiti = df_can.loc['Haiti', years] # passing in years 1980-2013 to exclude the 'Total' column
haiti.head()
haiti.plot()

#change the value of haiti to type integer for plotting
haiti.index = haiti.index.map(int)

##the code below is running well, but it seems no good
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrant')
plt.xlabel('Years')
plt.text(0.2, 0.6, '2010 Earthquake')
plt.show()

China_India = df_can.loc[['China', 'India'], years]
China_India
China_India.plot(kind='line')
df_CI = China_India.transpose()
df_CI
#df_CI_tes = df_CI.index.map(int)
df_CI.plot(kind='line')
#df_CI_tes(kind = 'line')
plt.title('Immigrant from China and India')
plt.ylabel('Number of Immigrant')
plt.xlabel('Years')
plt.show()
