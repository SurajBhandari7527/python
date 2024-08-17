# len,max,min,sum,sorted
s1={1,2,5,4,3,9,7,6}
s2={10,11}
print(len(s1))
print( sum( s1))
print(max(s1))
print( min(s1))
print( sorted(s1))      # it is sorted in list

# union/update
print(s1.union(s2))
s1.update(s2) #this is the defualt function which does union
print(s1 ) # s1 has changed
print(s2)

#union_update and intersection_update
s1={1,2,5,4,3,9,7,6}
s2={7,8,9,10,11}
s1.intersection_update(s2) #extracts the intersection and updates in s1
print(s1)
print(s2)

#difference_update
#this update combination is used to make permanent change to the original sets
s1={1,2,5,4,3,8,7,6}
s2={7,8,9,10,11}
s1.difference_update(s2)
print(s1)
print(s2)

#symmetric difference_update
s1={1,2,5,4,3,8,7,6}
s2={7,8,9,10,11}
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

#issubset/isdisjoint/issuperset
s1={1,2,3,4,5}
s2={2,3}
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s2.issubset(s1)) # can be read as: is s2 the subset of s1?
print(s2.issuperset(s1))
print(s1.issuperset(s2)) #is s1 superset of s2?

#copy function creates shallow copy
s1={1,2,3}
s2=s1.copy() #new set is made named s2 and elements copied to s2 from s1

print(s1)
print(s2)
print(id(s1))
print(id(s2)) 
