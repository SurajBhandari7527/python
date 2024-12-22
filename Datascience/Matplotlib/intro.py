'''types of data
1. Numerical data
2. Categorical data'''

#import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 2d plot 
#it is used for bivariate analysis of data
#it can be between categorical and numerical , numerical and numerical
#Use case- Time series data (any data that is related to the time)(like: how something is changing with time)

#Eg: plotting a simple data
price=[48000,54000,57000,49000,47000,45000]
year=[2015,2016,2017,2018,2019,2020]
plt.plot(year,price)
plt.show()