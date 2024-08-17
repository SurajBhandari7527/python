import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7, 8,9]])
arr1=np.array([3])
#when 2d and 1d(with single) element is added(notes in copy in detail)
print(arr+arr1)

# 2d and proper 1d array
arr1=np.array([1,2,3])
print(arr+arr1)

arr=np.array([[1,2,3],[4,5,6],[7, 8,9]])
arr1=np.array([2,3])
#print(arr+arr1) we cannot broadcast this arr is 3,3 while arr1 is 1,2 
#the requirement is either it should be single element or it should have no. of rows equal

arr=np.array([1,2,3])
arr1=np.array([[3],[2],[1]]);
print(arr+arr1)