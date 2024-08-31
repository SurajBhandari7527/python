import numpy as np
import pandas as pd
'''Series is 1D and DataFrames are 2D objects
But why?
And what exactly is index?'''
# can we have multiple index? Let's try
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a = pd.Series([1,2,3,4,5,6,7,8],index=index_val)
a

# The problem?
# a['cse']

# The solution -> multiindex series(also known as Hierarchical Indexing)
# multiple index levels within a single index

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex=pd.MultiIndex.from_tuples(index_val)
multiindex.levels[0]
multiindex.levels[1]

# 2. pd.MultiIndex.from_product()
pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]]) #this will do the cartesian product basically

# level inside multiindex object
# creating a series with multiindex object
s = pd.Series([1,2,3,4,5,6,7,8],index=multiindex)
s

# how to fetch items from such a series
s['cse']

# a logical question to ask
#but we can represent this by using dataframes too

# unstack
temp = s.unstack() #this converts the 2d multiframe series into dataframe
temp

# stack
temp.stack()
#to convert the dataframe created using unstack() into again multi index series# Then what was the point of multiindex series?
# why are we even doing this?
# the main thing is we can covert any high dimensional data into 2d i.e (5d,6d,20d into 2d)

# multiindex dataframe
branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiindex,
    columns = ['avg_package','students']
)

branch_df1

branch_df1['students']
# Are columns really different from index?
#pandas treats both in similar way

# multiindex df from columns perspective
branch_df2 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index = [2019,2020,2021,2022],
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

branch_df2

branch_df2.loc[2019]

# Multiindex df in terms of both cols and index

branch_df3 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

branch_df3
#lets now make our own multiindex dataframe which will have district and municipality in the index and school name and class in the column
index=[2023,2024]
df=pd.DataFrame([
        [10,8,3,15,10,12],
        [12,9,5,13,11,18],
        [10,8,3,15,10,12],
        [12,9,5,13,11,18]
    ],index=pd.MultiIndex.from_product([['Banganga','Kapilvastu'],["2023",'2024']]),columns=pd.MultiIndex.from_product([['A+','A'],["8","10","12"]]))
df

#single unstack
df.unstack()



#double unstack
df.unstack().unstack()
#this will convert the dataframe into 1d (index and value only)

'''Stacking and Unstacking
Working with multiindex dataframes'''

df.stack().stack()
#stack converts the column into row i.e(the inner column is converted into row)

# head and tail
branch_df3.head()
# shape
branch_df3.shape
# info
branch_df3.info()
# duplicated -> isnull
branch_df3.duplicated()
branch_df3.isnull()

# Extracting rows single
branch_df3.loc[('cse',2022)]

# multiple
branch_df3.loc[('cse',2019):('ece',2020):2] #extracting alternate rows
# using iloc
branch_df3.iloc[0:5:2]

# Extracting cols
branch_df3['delhi']['students']
#What if I say I want to extract the A+ of 10 class and A of 8 class
# df.iloc[:,1:4:2]
df.iloc[:,[1,3]] #fancy indexing
branch_df3.iloc[:,1:3]
# Extracting both
branch_df3.iloc[[0,4],[1,2]]

# sort index
# both -> descending -> diff order
# based on one level
branch_df3.sort_index(ascending=False)
branch_df3.sort_index(ascending=[False,True])
branch_df3.sort_index(level=0,ascending=[False])

# multiindex dataframe(col) -> transpose
branch_df3.transpose()  #this will make the column as row and rows as columns

#swapping the levels 
df #firstly see the df
df.swaplevel() #year becomes level 0 and the municipality becomes level 1

# swaplevel
branch_df3.swaplevel(axis=1)

'''Wide format is where we have a single row for every data point with multiple columns to hold the values of various attributes.

Long format is where, for each data point we have as many rows as the number of attributes and each row contains the value of a particular attribute for a given data point.'''

# melt -> simple example branch
# wide to long
pd.DataFrame({'cse':[120]}).melt()

# melt -> branch with year
pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}).melt(var_name='branch',value_name='num_students')


pd.DataFrame(
    {
        'branch':['cse','ece','mech'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    }
).melt(id_vars=['branch'],var_name='year',value_name='students')

# melt -> real world example
death = pd.read_csv('D:/python/Datascience/datasets/time_series_covid19_deaths_global.csv')
confirm = pd.read_csv('D:/python/Datascience/datasets/time_series_covid19_confirmed_global.csv')
print(death.head())
print(confirm.head())

#The aim is to find the data of Nepal in four columns country name, date, no. of confirmed cases, and no. of deaths in long row format

Nepal_confirm=confirm[confirm['Country/Region'].isin(['Nepal'])]
Nepal_death=death[death['Country/Region'].isin(['Nepal'])]
print(Nepal_confirm)
print(Nepal_death)
#for confirmed dataset
Nepal_confirm.set_index('Country/Region',inplace=True)
print(Nepal_confirm)
confirmed_cases=Nepal_confirm.iloc[:,3:1080:1].melt(var_name='Date',value_name='No. of confirmed cases')
print(confirmed_cases)

#for death dataset
Nepal_death.set_index('Country/Region',inplace=True)
print(Nepal_death)
death_cases=Nepal_death.iloc[:,3:1080:1].melt(var_name='Date',value_name='No. of death cases')
print(death_cases)

#merging both
final_dataset=confirmed_cases.merge(death_cases,how='inner',on='Date')
final_dataset['Country']='Nepal'
final_dataset.set_index('Country',inplace=True)
print(final_dataset)
