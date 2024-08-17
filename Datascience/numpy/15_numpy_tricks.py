import numpy as np
#append
arr=np.random.randint(1,20,15)
arr=arr.reshape(5,3)
print(arr)
print(np.shape(arr[:,0]))              #( 5     ,1)
arr=np.append(arr,np.random.random((arr.shape[0],1)),axis=1)
print(arr)

#expand dimensions
arr=np.random.randint(1,20,15)
print(arr)
print(arr.shape)
arr=np.expand_dims(arr,axis=0)
print(arr)
print(arr.shape)
arr=np.random.randint(1,20,15)
arr=np.expand_dims(arr,axis=1)
print(arr)
print(arr.shape)

#correlation coefficient
salary=np.array([25000,30000,35000,40000])
experience=np.array([1,2,4,7])
print(np.corrcoef(experience,salary))
