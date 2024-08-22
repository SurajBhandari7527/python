import pandas as pd
ipl=pd.read_csv('D:\python\Datascience\datasets\ipl-matches.csv')
movies=pd.read_csv('D:\python\Datascience\datasets\movies.csv')

#astype
print(ipl)
print(ipl.info())
#I want to change the ID into int 32
ipl['ID']=ipl['ID'].astype('int32')
ipl.info()

