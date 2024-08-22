import pandas as pd
ipl=pd.read_csv('D:\python\Datascience\datasets\ipl-matches.csv')
movies=pd.read_csv('D:\python\Datascience\datasets\movies.csv')

Family={'Name':['Suraj','Kiran','Krishna','Kamal','0','0'],'Age':['20','24','41','50','0','0'],'gender':['M','M','F','M','0','0']}
fam_dataframe=pd.DataFrame(Family)
print(fam_dataframe) 

#how to fetch a particular column
#title indexing

print(ipl['ID']) 
#actually one column of dataframe is a series
print(type (ipl['ID'])) #its really a pandas series

#what if we want 3 columns from the dataset
print(movies)
print(movies[['year_of_release','actors','title_x']]) #this is dataframe because it is multiple series
print(type(print(movies[['year_of_release','actors','title_x']])))


#how to fetch the rows
#iloc l(fetching using index)
print(fam_dataframe.iloc[0])
print(fam_dataframe.iloc[0:5])
print(fam_dataframe)

#fancy indexing

print(fam_dataframe.iloc[[1,2,4]])

#loc(fetching using labels) (but the index should be string)
fam_dataframe.set_index('Name',inplace=True)
print(fam_dataframe.loc['Suraj'])
print(fam_dataframe.loc['Suraj':'Krishna'])
#even if our own index is given. there is still the pandas default index of 0,1,2,3...so we can also use iloc and fancy indexing with iloc always
#but we can't use loc if custom index is not given

#what if i want to fetch 2 rows and 2 columns only?
print(fam_dataframe.iloc[0:2,0:2])
#loc can also be used similarly

