#1. empty set
s={} #it is wrong way
print( type(s)) #its dictionary because set and dictionary both have the same syntax
#to create empty set
s1=set({})  #typecasting
print(type(s1))

#1D and 2D sets
s2={1,2,3}
# s3={1,2,{3,4}}     this is not possible to create. this will throw error

# homo and hetero sets
s3={5,4,3,2,1}  #the order of elements in output is assigned acc to hash number called hashing.we don't have control of the position
s4={1,2,True,5.6,'suraj',2.2} # true means 1 so, both 1 and true cannot get printed because no duplicates allowed in sets
print(s3)
print(s4)


#type conversion to create set
 
s5=set([1,2,3])  #create set from list by type conversion
print(s5)


#2d set using frozenset
'''Question: Why can't you include a set inside another set in Python?

Answer:

In Python, sets are collections of unique, hashable elements. The reason you can't include 
a set inside another set is because sets themselves are mutable. 
Since mutable objects can change, they can't have a fixed hash value, which is required for an object to be hashable.'''
fs1=frozenset([1,2,3,frozenset([4,5,6])])
print(fs1)

#set comprehension
print({i for i in range(1,11)})