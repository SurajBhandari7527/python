import numpy as np
arr1=np.round(np.random.random((4))*100)
arr2=np.round(np.random.random((3,3))*100)
arr3=np.round(np.random.random((3,3,3))*100)

#for loop in 1d array
for i in arr1:
    print(i)  #this prints all the elements

#for loop in 2d array
for i in arr2:
    print(i) # this prints the elements in 1 d array by each row

#for loop in 3d array
for i in arr3:
    print(i) #this prints the elements in 2d array 
    
#how to iterate over each element in the array
for i in np.nditer(arr3):
    print(i)
