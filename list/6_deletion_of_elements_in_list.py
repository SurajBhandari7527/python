#del
a=[1,2,3,4]
del a # full list is deleted. not in the memory level but we can resemble like full list is deleted 


# remove
a=[1,2,3,4,5] 
a.remove(3) # when we don't know the position of element to be removed but we know what is to be removed. removes by searching the element


#pop
b=[1,2,3,4,5]
b.pop() #this removes the last element of the list
print(b)
#it can be used to delete specific element to by providing the index of the element inside the bracket
b=[1,2,3,4,5]
b.pop(0)
print(b)


#clear
b=[1,2,3,4,5]
b.clear() #it converts any list into empty list
print(b)