import pandas as pd
import numpy as np
top_movies=pd.read_csv('D:\python\Datascience\datasets\imdb-top-1000.csv')
print(top_movies)
movie_group=top_movies.groupby('Genre')

mean=movie_group.mean(numeric_only=True)
print(mean)
print(movie_group.min())
print(movie_group.sum())
print(movie_group.std(numeric_only=True))

print(top_movies.columns)
print(top_movies['Gross'])
print(movie_group['Gross'].sum().sort_values(ascending=False).head())

#find the name of genre which has highest avg imdb rating
print(top_movies.columns)
print(movie_group['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

#find the name of director which is most popular
print(top_movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))

#find the highest rated movie of each genre
print(movie_group[['Series_Title','IMDB_Rating']].max(numeric_only=True).sort_values(by='IMDB_Rating',ascending=False))

#find the no.of movies each actor has played
print(top_movies.groupby('Star1').count()['Series_Title'].sort_values(ascending=False))































































































































