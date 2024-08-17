import numpy as np
arr=np.random.random((5,3))
arr=arr*100
print(arr)

#sum,max,min,product
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.prod(arr))

#to find the max value in the row and max value in the column
print(np.max(arr,axis=1)) # max value in each row
print(np.max(arr,axis=0)) # max value in each column
# same for min

#mean/median/standard deviation/variance
print( np.mean(arr,axis=0))
print(np.median(arr,axis=0))
print(np.std(arr,axis=0))
print(np.var(arr,axis=0),'\n')

#trigonometric functions
print(np.sin(arr))

#dot product of the matrix
arr1=np.random.random((3,5))
arr1=arr1*100
print(np.dot(arr,arr1)) 

#log and exponents
print(np.log(arr))
print(np.exp(arr))

#round/floor/ceil
arr=np.round(arr)
arr1=np.floor(arr1)
arr2=np.ceil(arr1)
print(arr,'\n')
print(arr1,'\n')
print(arr2,'\n')

#reshaping functions(imp)
#reshape

arr=np.arange(1,11).reshape((5,2))
print(arr)

#transpose
print(np.transpose(arr))
print(arr.T)

#ravel( to convert any 2d or 3d array into 1 d)
print(np.ravel(arr))
