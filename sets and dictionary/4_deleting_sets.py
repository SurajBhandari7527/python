s={1,2,3,4,5,6}
del s   # whole set is deleted
s={1,2,3,4,5,6}
s.discard(4)
print(s)       # to remove 1 element by specifying the element
s.remove(3)
print(s)       # same as discard 
# the diff is discard doesn't throw error when given an element not present in the set but remove does throw error
s.discard(20) # no error
# s.remove(20) this throws error

s.pop()   # it deletes a random element 
print(s)
