# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:43:01 2020

@author: user
"""

##Training Python Sesi 5: PANDAS

import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')
len(df)
df.shape
df.head()
df.tail()
pd.set_option('display.max.columns', None)
pd.set_option('display.precision', 2)
df.info()

##showing basic statistics
df.describe()

#exploring dataset
df['team_id'].value_counts() ##menghitung banyaknya masing2 komponen dalam "team-id"
df['fran_id'].value_counts()
df.loc[df['fran_id'] == 'Lakers', 'team_id'].value_counts()
df.loc[df['team_id'] == 'MNL', 'date_game'].min()
df.loc[df['team_id'] == 'MNL', 'date_game'].max()
df.loc[df['team_id'] == 'MNL', 'date_game'].agg(('min', 'max'))
df.loc[df['team_id'] == 'BOS', 'pts'].sum()

#understanding series object
revenues = pd.Series([5555, 7000, 1980])
revenues.values
revenues.index
city_revenues = pd.Series(
        [4200, 8000, 6500],
        index=['Amsterdam', 'Toronto', 'Tokyo']
        )
city_revenues

city_employee_count = pd.Series({'Amsterdam': 5, 'Tokyo': 8})
city_employee_count
city_employee_count.keys()
'Tokyo' in city_employee_count
'New York' in city_employee_count

#understanding DataFrame objects
city_data = pd.DataFrame({
        'revenues': city_revenues,
        'employee_count': city_employee_count
        })
city_data
city_data.index
city_data.values
city_data.axes
city_data.axes[0]
city_data.axes[1]
city_data.keys()
'Amsterdam' in city_data
'revenues' in city_data


df.index
df.axes
'points' in df.keys()
'pts' in df.keys()

##df_radiosonde = pd.read_csv('C:\tes\python\data-contoh\data-radiosonde-2.csv')