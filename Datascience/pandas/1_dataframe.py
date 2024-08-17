#create  dataframe
import pandas as pd
L=[['Suraj','20','M'],['kiran','24','M'],['Krishna','41','F'],['Kamal','50','M']]
data=pd.DataFrame(L,columns=['Name','Age','Gender'])
print(data)

#we can do the same using dictionary as well
Family={'Name':['Suraj','Kiran','Krishna','Kamal'],'Age':['20','24','41','50'],'gender':['M','M','F','M']}
fam_dataframe=pd.DataFrame(Family)
print(fam_dataframe) #for dictionary no need to specify the column name.it will automatically fetch the key and use it as column name

ipl=pd.read_csv('D:\python\Datascience\datasets\ipl-matches.csv')
movies=pd.read_csv('D:\python\Datascience\datasets\movies.csv')

#shape
print(ipl.shape)

#dtypes  
print(ipl.dtypes)#this return the datatype of all the columns.pandas write object for string datatype

#index
print(ipl.index) #here the index is generated automatically

#columns
print(ipl.columns)
print(movies.columns)

# values
