import pandas as pd
import numpy as np
top_movies=pd.read_csv('D:\python\Datascience\datasets\imdb-top-1000.csv')
print(top_movies)


#duo categorized group
movie_group=top_movies.groupby(['Director','Star1'])
print(movie_group.groups)
print(top_movies.columns)

#fetch which duo of director and star made the maximum gross
print(movie_group['Gross'].sum().sort_values(ascending=False).head(1))
print('The movie details\n\n')

#best actor-genre combo based on metascore(avg)
actor_genre=top_movies.groupby(['Star1','Genre'])
print(actor_genre['Metascore'].mean().sort_values(ascending=False).head(1))


