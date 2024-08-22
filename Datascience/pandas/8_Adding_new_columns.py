import pandas as pd
ipl=pd.read_csv('D:\python\Datascience\datasets\ipl-matches.csv')
movies=pd.read_csv('D:\python\Datascience\datasets\movies.csv')

Family={'Name':['Suraj','Kiran','Krishna','Kamal','0','0'],'Age':[20,23,41,50,0,0],'gender':['M','M','F','M','0','0']}
fam_dataframe=pd.DataFrame(Family)
print(fam_dataframe) 

movies['column']='India'
print(movies)
#this will add a new column which will contain India in each row
 
 #I want to make a new column named 'lead actor' which will contain the first(main) actor from the 'actors'
#firstly lets replace the missing values with 'None'
movies.fillna('None',inplace=True)
movies['Lead_actor']=movies['actors'].str.split('|').apply(lambda x: x[0])
print(movies['Lead_actor'])
print(movies[movies['Lead_actor']=='None'])