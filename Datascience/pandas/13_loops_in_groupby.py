import pandas as pd
import numpy as np
top_movies=pd.read_csv('D:\python\Datascience\datasets\imdb-top-1000.csv')
print(top_movies)
movie_group=top_movies.groupby('Genre')

movie_movie_group=top_movies.groupby('Genre')
#loops in movie_groups 
#finding the highest rated movies from their own genre for all genres 
df=pd.DataFrame(columns=top_movies.columns)
for movie_group,data in movie_movie_group:
        df = pd.concat([df,data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]],ignore_index=True)
print(df)
