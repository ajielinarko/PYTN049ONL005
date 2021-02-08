# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:44:20 2021

@author: user
"""

#Rabu, 6 Januari 2020
#Training Python Sesi 11: Introduction to Machine Learning

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linier_model import LinearRegression

#%matplotlib inline

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

print(x)
print(y)

model = LinearRegression()

model.fit(x,y)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
                 normalize=False)
