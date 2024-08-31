import numpy as np
import pandas as pd

courses=pd.read_csv("D:\python\Datascience\datasets\courses.csv")
students=pd.read_csv("D:\python\Datascience\datasets\students.csv")
nov=pd.read_csv('D:/python/Datascience/datasets/reg-month1.csv')
dec=pd.read_csv("D:/python/Datascience/datasets/reg-month2.csv")

matches=pd.read_csv("D:\python\Datascience\datasets\matches.csv")
delivery=pd.read_csv("D:\python\Datascience\datasets\deliveries.csv")

print(courses)
#pd.concat
combined_regs=(pd.concat([nov,dec],ignore_index=True))
print(combined_regs)
#if ignore_index is not used it will use the index of the above dataframe after concateneting vertically

# #append
# nov.append(dec,ignore_index=True) this doesnot work anymore ignore

#multi index
multi_index=pd.concat([nov,dec],keys=['Nov','Dec'])
print(multi_index) #the data will be spilted into two indices with different key name nov and dec
#how to fetch from multi index
#first data from nov
print(multi_index.loc[('Nov',0)])


#if I want to concatenate/join the two dataframes horizontally
horizontal=pd.concat([nov,dec],axis=1)
print(horizontal) #the index no. is taken from the nov(if not enough then added)





