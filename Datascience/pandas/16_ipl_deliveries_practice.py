import numpy as np
import pandas as pd
ipl_deliveries=pd.read_csv('D:\python\Datascience\datasets\deliveries.csv')

print(ipl_deliveries.columns)

#find the top 10 batsman in terms of batting
print(ipl_deliveries.head(10))
print(ipl_deliveries[ ['wide_runs','bye_runs', 'legbye_runs', 'noball_runs', 'penalty_runs','batsman_runs', 'extra_runs', 'total_runs']])

batsman=ipl_deliveries.groupby('batsman')
print(batsman['batsman_runs'].sum().sort_values(ascending=False).head(10))

#find the batsman with highest no. of sixes
sixes=ipl_deliveries['batsman_runs']==6
sixes_data=ipl_deliveries[sixes]
print(sixes_data)
only_six_of_batsman=sixes_data.groupby('batsman')
print(only_six_of_batsman['batsman_runs'].count().sort_values(ascending=False).head(1))

#find batsman with most number of 4's and 6's in last 5 overs
print(ipl_deliveries['over'])
last_5_over_boolean=(ipl_deliveries['over']>15) & ((ipl_deliveries['batsman_runs']==4) | (ipl_deliveries['batsman_runs']==6))
last_5_over=ipl_deliveries[last_5_over_boolean]
print(last_5_over['over'])
four_sixes_of_batsman=last_5_over.groupby('batsman')
print(four_sixes_of_batsman['batsman_runs'].sum().sort_values(ascending=False).head(3))

 #virat kohli record against all the teams
virat_kohli=ipl_deliveries[ipl_deliveries['batsman']=='V Kohli']
print(virat_kohli)
opponent=virat_kohli.groupby('bowling_team')
print(opponent['batsman'].head())
print(opponent['batsman_runs'].sum().sort_values(ascending=False))








