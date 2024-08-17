a=[1,2,3,4,5]
a.append(6) #this adds 6 to the list. whatever is inside the bracket is considered as one element that is appended
print(a)

a.extend([7,8]) #this adds both the lists elements on one
print(a)

a.append([9,10,11]) #it adds whole list as one element
print(a)

#predict the output
a.extend('hello')
print(a)

b=[5,4,3,2,1]
b.insert(0,6)
print(b)