# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:08:34 2020

@author: user
"""

##Training Python Sesi 6: PANDAS EPS. 2 EXPLANATORY DATA ANALYSIS

#Data cleaning with Pandas
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/property_data.csv')
#df = pd.read_csv('C:\tes\python\data-contoh\data-contoh-sesi6.csv')
df
df.head(10)

#to see how Pandas handle missing values
df['ST_NUM']    #Pandas mengisi ruang kosong dengan "NA"
df['ST_NUM'].isnull() #the output is True atau False

df['NUM_BEDROOMS']
df['NUM_BEDROOMS'].isnull()

missing_values = ['na', 'n/a', '--']
dg = pd.read_csv(r'C:\tes\python\data-contoh\data-contoh-sesi6.csv', na_values = missing_values)
dg
dg['NUM_BEDROOMS']
dg['NUM_BEDROOMS'].isnull()

#un-expected missing values
dg['OWN_OCCUPIED']  #pada kolom ini jenis missing value adalah kesalahan input
                    #dari seharusnya 'char' (Y/N) menjadi 'int' (12)
                    #sehingga pandas tidak mendeteksi adanya missing value dgn tepat
dg['OWN_OCCUPIED'].isnull()

#code untuk mengatasi masalah un-expected missing values
#see kode.id/sesi 6 untuk membaca strategi pemecahan masalahnya
cnt = 0
for row in dg['OWN_OCCUPIED']:
    try:
        int(row)
        dg.loc[cnt, 'OWN_OCCUPIED'] = np.nan
    except ValueError:
        pass
    cnt+=1

dg.head(9)

#summarizing missing values
dg.isnull().sum()           #melihat jumlah total missing values u/ setiap feature
dg.isnull().values.any()    #melihat apakah memiliki nilai yg hilang sama sekali
dg.isnull().sum().sum()     #mendapatkan jumlah total missing values

#replacing
dg['ST_NUM'].fillna(125, inplace=True)  #mengganti missing value dgn int 125
dg['ST_NUM']
df.loc[2, 'ST_NUM'] = 125               #mengganti missing value pada lokasi tertentu
df['ST_NUM']
#mengganti missing values dgn median
median = dg['NUM_BEDROOMS'].median()
dg['NUM_BEDROOMS'].fillna(median, inplace=True)
dg

#analyzing obesity in England
data = pd.ExcelFile(r'C:\tes\python\data-contoh\obes-sesi6.xls')
data.sheet_names

#dari file obes-sesi6.xls, kita hanya akan membuka sheet 7.2
# dan hanya membutuhkan baris ke-5 s/d 18  
data_age = data.parse(u'7.2', skiprows=4, skipfooter=14)
data_age.head()

#me-rename the first header
data_age.rename(columns={u'Unnamed: 0': u'Year'}, inplace=True)
#menghilangkan empty rows
data_age.dropna(inplace=True)
#mengubah 'indeks angka' menjadi tahun agar mudah saat di plot
data_age.set_index('Year', inplace=True)
#plotting
data_age.plot()
data_age_minus_total = data_age.drop('Total', axis=1)
data_age_minus_total.plot()

#plot specific column


##TIME SERIES
#Basic time series manipulation
from datetime import datetime
import pandas as pd
import numpy as np

date_rng = pd.date_range(start='1/01/2020', end='1/08/2020', freq='H')
date_rng

#membuat data frame dengan timestamp per jam
df = pd.DataFrame(date_rng, columns=['date'])
df 
df['data'] = np.random.randint(0,100,size=(len(date_rng)))
df.head()
df['datetime'] = pd.to_datetime(df['date'])
