#similar as in string

#len,max,min,sorted ( Normal functions)
b=[1,2,3,4,5]
print(len(b),"len")
print(sum(b),'sum')
print(max(b),"max")
print(min(b),"min")
print(sorted(b),'sorted')                                   #new sorted list is created without affecting the original one
print(sorted(b,reverse=True),'sorted in descending order')  # new list is created
b.sort()              # The original list is replaced with sorted list. new list is not created.understand sorted(b) vs b.sort
print(b)

print(b.count(2),'count')
print(b.index(4),'index')
b.reverse()                      #it affects the permanently the original list
print(b)

#copy
b=[1,2,3,4,5]
print(b,'original one')
print(id(b),'original one id')
b1=b.copy()
print(b1,'copied one')
print(id(b1),'copied one id') # that means a shallow copy is created and original is not affected
