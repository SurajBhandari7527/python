import pandas as pd
import numpy as np
top_movies=pd.read_csv('D:\python\Datascience\datasets\imdb-top-1000.csv')
print(top_movies)
movie_group=top_movies.groupby('Genre')

#aggregate methods(if we want to apply diff functions/calculations for different columns)
print(movie_group.agg({'Runtime':'mean','IMDB_Rating':'mean','No_of_Votes':'sum','Gross':'sum','Metascore':'min'}))
#we can also do multiple calculations for a single column by passing the functions to the list 
print(movie_group[['IMDB_Rating','Gross','Runtime','No_of_Votes','Metascore']].agg(['min','max','mean']))#this will calculate min max and sum value for each columns 
#we can combine both
print(movie_group.agg({'Runtime':['min','max','mean'],'IMDB_Rating':['min','max','mean'],'No_of_Votes':['min','max','mean'],'Gross':['min','max','mean'],'Metascore':['min','max','mean']}))
