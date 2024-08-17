d2={'name':'Suraj Bhandari','course':'B.Tech','sem':4,'subjects':{'dsa':95,'maths':90,'architecture':80}}
print(len(d2))
print(max(d2))
print(min(d2))
print(sorted(d2)) #sorting only prints the list of keys 


#items
print(d2.items())
#It converts the key value pair into list of tupples

#keys 
print(d2.keys())    #prints the list of keys

#values
print(d2.values())   #prints the list of values

# update 
d1 = {1:2,3:4,4:5}
d2 = {4:7,6:8}
d1.update(d2) #basically, it can be used to union both dictionaries
print (d1)
