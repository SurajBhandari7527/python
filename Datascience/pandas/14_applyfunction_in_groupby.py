import pandas as pd
import numpy as np
top_movies=pd.read_csv('D:\python\Datascience\datasets\imdb-top-1000.csv')
print(top_movies)

movie_movie_group=top_movies.groupby('Genre')

#apply fucntion
print(movie_movie_group.apply(max))
def check(series):
            print(series.str.startswith('A').sum())
movie_movie_group['Series_Title'].apply(check)

#find the rank of movies inside their own genre
def rank_movie(group): 
        group[ 'rank'] = group[ 'IMDB_Rating'].rank(ascending=False)
        return group[group['rank']==1.0]
whatever=movie_movie_group.apply(rank_movie)  
print(whatever)

#find normalization of the imdb rating 
def normalization(series_normalize):
        series_normalize['Normalized']=(series_normalize['IMDB_Rating']-series_normalize['IMDB_Rating'].min())/(series_normalize['IMDB_Rating'].max()-series_normalize['IMDB_Rating'].min())
        return series_normalize

series_normalize=movie_movie_group.apply(normalization,include_groups=True)    
print(series_normalize) 

