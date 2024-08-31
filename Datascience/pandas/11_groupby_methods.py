import pandas as pd
import numpy as np
top_movies=pd.read_csv('D:\python\Datascience\datasets\imdb-top-1000.csv')
print(top_movies)
movie_group=top_movies.groupby('Genre')

#how do we know that how many movie_groups are formed?
print(len(movie_group))
 
#how to know how many rows in each movie_group
print(movie_group.size()) #inbuilt(preferrable)
print(movie_group['Series_Title'].count()) #pandas function

#how to fetch the first movie of each movie_group
print(movie_group.first()['Series_Title']) 
print(movie_group.last()['Series_Title'])  #fetch the last movie of each movie_group
print(movie_group.nth(6)['Series_Title'])  #fetch the 6th movie of each movie_group
print(movie_group.nth(0)['Series_Title']) #fetch the 0th movie of each movie_group (that means fetching of nth means nth acc to indexing position)

#to see all the datas in a certain movie_group
print(movie_group.get_group('Action'))

#to see which movie_group datas has taken which index positions
print(movie_group.groups)

#TO GET mathematical analysis of different movie_groups
print(movie_group.describe())

#sample (to see sample of movie_groups)
#I want to see two movies from each genre
print(movie_group.sample(2,replace=True)) #replace=True will repeat the same movie if movie_group contains a single movie

#no of unique values
print(movie_group.nunique())