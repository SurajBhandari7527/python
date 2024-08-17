import numpy as np
arr=np.random.randint(1,11,10).reshape((5,2))
print(arr)
#fancy slicing( it can be used to extract specific rows or columns when its not in any order)
#extract 2,4,5 row
print(arr[[1,3,4],:])
arr=arr.reshape(2,5)
#extract 2,4,5 column
print(arr)
print(arr[:,[1,3,4]])

#boolean slicing(very powerful and important)
print(arr>2) #this returns the boolean matrix after comparing each element with the given condition
print(arr[arr>2]) #the list of the elements in the matrix arr is printed in 1 d array which satisfies the condition

