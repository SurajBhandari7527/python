#create  dataframe
import pandas as pd
L=[['Suraj','20','M'],['kiran','24','M'],['Krishna','41','F'],['Kamal','50','M']]
data=pd.DataFrame(L,columns=['Name','Age','Gender'])
print(data)

#we can do the same using dictionary as well
Family={'Name':['Suraj','Kiran','Krishna','Kamal','0','0'],'Age':['20','24','41','50','0','0'],'gender':['M','M','F','M','0','0']}
fam_dataframe=pd.DataFrame(Family)
print(fam_dataframe) #for dictionary no need to specify the column name.it will automatically fetch the key and use it as column name

ipl=pd.read_csv('D:\python\Datascience\datasets\ipl-matches.csv')
movies=pd.read_csv('D:\python\Datascience\datasets\movies.csv')

#shape
print(ipl.shape) #this returns the no of rows and columns

#dtypes  
print(ipl.dtypes)#this return the datatype of all the columns.pandas write object for string datatype

#index
print(ipl.index) #here the index is generated automatically
fam_dataframe.set_index('Name')
print(fam_dataframe,'changing index')

#columns
print(ipl.columns) #lists all the columns
print(movies.columns)

#sample
print( ipl.sample) #to fetch 5 random datas

# values
print(ipl.values) # this will return 2d numpy array of only values

#head and tails
#(same as in pandas series)
print(ipl.head())
print(ipl.tail())



print(fam_dataframe.duplicated())
print(fam_dataframe[fam_dataframe.duplicated()])













