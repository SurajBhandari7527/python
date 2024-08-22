import pandas as pd
ipl=pd.read_csv('D:\python\Datascience\datasets\ipl-matches.csv')
movies=pd.read_csv('D:\python\Datascience\datasets\movies.csv')

Family={'Name':['Suraj','Kiran','Krishna','Kamal','0','0'],'Age':[20,23,41,50,0,0],'gender':['M','M','F','M','0','0']}
fam_dataframe=pd.DataFrame(Family)
print(fam_dataframe) 

#i want to fetch the data of the people of my family whose age is more than 20
above_20=fam_dataframe['Age'] > 20
print(fam_dataframe[above_20])

#how many matches won by csk in kolkata
print(ipl.columns)
print(ipl['WinningTeam'].head(20))
print(ipl['City'])

print(ipl[(ipl['WinningTeam']=='Chennai Super Kings') & (ipl['City']=='Kolkata')].shape[0],'matches won by csk in kolkata')

#what is the percentage of toss won and matchwon ?
print(ipl[['TossWinner','WinningTeam']])

toss_win_game_win=ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]
print(toss_win_game_win)

toss_win_game_lost=ipl.shape[0]-toss_win_game_win
print(toss_win_game_lost)
#or
print(ipl[ipl['TossWinner']!=ipl['WinningTeam']].shape[0])

percentage_of_toss_win_game_win=(toss_win_game_win/(toss_win_game_win+toss_win_game_lost)*100)
print(percentage_of_toss_win_game_win,'% matches are toss win game win')

#I am gonna fetch those movies which have higher rating than 8.5 and have more than 10000 rating reviews

print(movies.columns)
print(movies['imdb_votes'])
print(movies['imdb_rating'])
op_movies=movies[(movies['imdb_votes']>1000) & (movies['imdb_rating']>8)]
print(op_movies['title_x'])

#fetch actions movies whose genre is Action and rating is higher than 7.5

print(movies['genres'])
string=movies['genres'].str.split('|')
print(string)
action_movies=movies[('Action' in string) & (movies['imdb_rating']>7.5)] #in relational operator cannot be applied directly
print(action_movies['title_x'])
#this didnot work because in cant be applied

mask1=movies['genres'].str.split('|').apply(lambda x: 'Action' in x)
mask2=movies['imdb_rating']>7.5
print(movies[mask1 & mask2])
print(movies[mask1 & mask2]['genres'])
print(movies[mask1 & mask2]['genres'].shape[0])

mask1=movies['genres'].str.contains('Action')
print(movies[mask1 & mask2]['genres'])
print(movies[mask1 & mask2].shape[0])

