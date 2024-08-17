#create numpy array
#1D
import numpy as np
arr=np.array([1,2,3]) 
print(arr)
print(type(arr))
#2D
arr1=np.array([[1,2,3],[4,5,6]],dtype=float)
print(arr1)

#3D
arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)

#dtype
arr3=np.array([1,2,3.5],dtype=float) #it is converted to float data type.can create boolean,complex etc
print(arr3)

#arange ( same as range function)
print(np.arange(1,11))

#resize to create matrix
arr4=np.arange(1,11).reshape(5,2) #this will shape it to the matrix of order 5,2
print(arr4)

#initialize array with one
arr5=np.ones((3,3))
print(arr5)

#initialize array with zeros
arr6=np.zeros((3,3))
print(arr6)

#initialize arrray with random number with 0 to 1
arr7=np.random.random((3,3))
print(arr7)
arr7=np.random.randint(1,20,10)
print(arr7)

#linspace
arr8=np.linspace(1,20,8)
print(arr8)
# this create the list of 8 elements from 1 to 20 with equal difference i.e AP

#create identity matrix
arr9=np.identity(3,dtype=int)
print(arr9)

#to find dimention of a numpy array
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)

#to find the order of the array/matrix
print(arr.shape)
print(arr1.shape)
print(arr2.shape)

#to find the number of elements inside the matrix
print(arr.size)
print(arr1.size)
print(arr2.size)

#to know how much size each item is taking in the array
print(arr.itemsize) #default is int64 which takes 8 bytes while int32 takes 4 bytes
print(arr1.itemsize) 
print(arr2.itemsize)

#to know the datatype of the elements inside the array
print(arr.dtype)
print(arr1.dtype)
print(arr2.dtype)
