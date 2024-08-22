import pandas as pd
ipl=pd.read_csv('D:\python\Datascience\datasets\ipl-matches.csv')
#info
print(ipl.info())
#this will tell how many rows non null values are there in each column and their data types
#lastly it also tells how many columns have same data types and memory occupied as well

#describe
print(ipl.describe()) # same as in series

#isnull
print(ipl.isnull()) #this returns the whole dataframe by replacing the null values with true and occupied one with false

print(ipl.isnull().sum()) # this will return how many values in each row are true 
print(True+True)# oh it is equal to 2 that means true is considered as 1 while adding and false as 0

#duplicated
print(ipl.duplicated()) #it returns if there are duplicate rows in dataframe or not if not all value false
print(ipl.duplicated().sum(),'duplicates') #it returns how many duplicate rows are there in the dataset