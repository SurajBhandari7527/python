import numpy as np
arr1=np.round(np.random.random((3))*100)
arr2=np.round(np.random.random((3,3))*100)
arr3=np.round(np.random.random((3,3,3))*100)

#indexing 1D
print(arr1,'indexing in 1D')
print(arr1[0])
print(arr1[1])
print('\n')
#indexing in 2D
print(arr2,'indexing in 2D')
print(arr2[1,2])
print(arr2[1,0])
print('\n')

#indexing in 3D
print(arr3,'indexing in 3d')
print(arr3[1,2,2])
print(arr3[0,1,2])
print('\n')

#slicing in 1D
print(arr1,'slicing in 1d')
print(arr1[0:2]) #its the same as in the list
print('\n')

#slicing in 2D
print(arr2,'slicing in 2d')
print(arr2[0,:]) #to print the first row
print(arr2[:,0]) #prints the first column
print('\n')
#what if I want to extract[5,6,8,9] from [[1,2,3],[4,5,6],[7,8,9]]
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[1:,1:3])
#how to extract 1,3,7,9
print(arr[0::2,:3:2])

#slicing in 3d 
print(arr3) # this has 3 2d matrices
#what if I want to print the 2nd row of the 2nd 2d matrix
print(arr3[1,1,:]) #its the same as arr3[1:2:1,1:2:1,0:3:1]
#what if I want to print the middle column of the 2nd 2d matrix
print(arr3[1:2:1,0:3:1,1:2:1])
#what if I want to print the last four elements making square in the 3rd 2d matrix
print(arr3[2:3:1,1:3:1,1:3:1],'\n')
#what if I want to print the top two (right and left) elements of first row of 1st and 3rd 2d array
print(arr3[0:3:2,0:1:1,0:3:2])
