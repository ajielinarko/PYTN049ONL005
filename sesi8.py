# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 19:29:54 2020

@author: user
"""

##Training Python Sesi 8: Advanced Visualization

import numpy as np
import pandas as pd
from PIL import Image

df_can = pd.read_excel(r'C:\tes\python\data-contoh\Canada-data-contoh-sesi7.xlsx',
                       sheet_name = 'Canada by Citizenship',
                       skiprows = range(20),
                       skipfooter = 2)
print('Data read into a pandas dataframe')
df_can.head()
print(df_can.shape)

#clean up the dataset to remove unnecessary columns
df_can.drop(['AREA', 'DEV', 'REG', 'Type', 'Coverage'], axis = 1, inplace=True)

#let's rename the columns so that they make sense
df_can.rename (columns = {'OdName': 'Country',
                          'AreaName': 'Continent',
                          'RegName': 'Region'}, inplace = True) 

#for the sake of consistency, let's also make all column labels of type string
df_can.columns = list(map(str, df_can.columns))

#set the country name as index - useful for quickly looking up countries using .loc method
df_can.set_index('Country', inplace = True)

#add Total column 
df_can['Total'] = df_can.sum(axis=1)

#years that we will be using in this lesson - useful for plotting later on
years = list(map(str, range(1980, 2014)))
print('data dimension:', df_can.shape)

##VISUALIZING DATA USING MATPLOTLIB
%matplotlib inline

import matplotlib as mpl

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

mpl.style.use('ggplot')

#Waffle Charts
df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]
df_dsn

total_values = sum(df_dsn['Total'])
category_proportions = [(float(value) / total_values) for value in 
                        df_dsn['Total']]
for i, proportion in enumerate(category_proportions):
    print(df_dsn.index.values[i] + ': ' + str(proportion))

width = 40
height = 10
total_num_tiles = width * height
print('Total number of tiles is', total_num_tiles)

tiles_per_category = [round[proportion * total_num_tiles] for proportion in
                      category_proportions]
for i, tiles in enumerate(tiles):
    
#    ..... lanjut lagi nanti ....

##WORD CLOUDS
from wordcloud import WordCloud, STOPWORDS

print('WordCloud is installed and impoerted')    
!wget --quiet https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/alice_novel.txt -O alice_novel.txt    
    
    
    



