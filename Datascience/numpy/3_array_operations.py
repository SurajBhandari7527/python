import numpy as np
arr1=np.arange(1,13).reshape((3,4))
arr2=np.arange(10,22).reshape((3,4))
print(arr1)
print(arr2)

#scalar operations
#arithmetic operation
print(arr1+2)
print(arr1*2)
print(arr1/2)
print(arr1**2)

#relational operators 
print(arr1>5)
print(arr2>5) # this checks all the elements of the matrix if all the elements are greater than 5 or not


#Vector operations
#addition
print(arr1+arr2)
#subtraction
print(arr2-arr1)
#multiply
print(arr1*arr2)  #this is not matrix multiplication the corresponding elements are multiplied
#power
print(arr1**arr2) 

