# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 19:33:32 2021

@author: user
"""

#Senin, 4 Januari 2020
##Training Python Sesi 9: Descriptive Statistics
##dalam kondisi demam dan sakit persendian seluruh tubuh

import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
x = {8.0, 1, 2.5, 4, 28.0}
x_with_nan = {8.0, 1, 2.5, math.nan, 4, 28.0}
print(x)
print(x_with_nan)
y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(y)
print(y_with_nan)
print(z_with_nan)
