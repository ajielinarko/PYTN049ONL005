# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:41:49 2021

@author: user
"""

#Selasa, 5 Januari 2020
##Training Python Sesi 10: Inferential Statistics
##dalam kondisi demam dan sakit persendian seluruh tubuh

import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(5, 5)})

##Uniform Distribution
from scipy.stats import uniform
n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc = start, scale=width)
ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})
ax.set(xlabel='Uniform Distribution', ylabel='Frequency')

##Normal Distribution
from scipy.stats import norm
data_normal = norm.rvs(size=10000,loc=0,scale=1)
ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={'linewidth': 15, 'alpha': 1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')

##Gamma Distribution
from scipy.stats import gamma
data_gamma = gamma.rvs(a=5, size=10000)
ax = sns.distplot(data_gamma,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={'linewidth': 15, 'alpha': 1})
ax.set(xlabel='Gamma Distribution', ylabel='Frequency')

##Exponential Distribution
from scipy.stats import expon
data_expon = expon.rvs(scale=1, loc=0, size=1000)
ax = sns.distplot(data_expon,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={'linewidth': 15, 'alpha': 1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')

##Poisson Distribution
from scipy.stats import poisson
data_poisson = poisson.rvs(mu=3, size=10000)
ax = sns.distplot(data_poisson,
                  bins=30,
                  kde=False,
                  color='skyblue',
                  hist_kws={'linewidth': 15, 'alpha': 1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')

##Binomial Distribution
from scipy.stats import binom
data_binom = binom.rvs(n=10, p=0.8, size=10000)
ax = sns.distplot(data_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={'linewidth': 15, 'alpha': 1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')

##Bernoulli Distribution
from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000, p=0.6)
ax = sns.distplot(data_bern,
                  kde=False,
                  color='skyblue',
                  hist_kws={'linewidth': 15, 'alpha': 1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')

##Confidence Interval for the population proportion in python
import pandas as pd
import numpy as np
from google.colab import files
df = pd.read_csv(url)