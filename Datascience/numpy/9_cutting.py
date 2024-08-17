#array can be cut horizontally or vertically
#hsplit
import numpy as np
arr2=np.round(np.random.random((4,4))*10)
print(arr2)
arr=np.hsplit(arr2,2) #split horizontally arr2 into 2 equal parts
print(arr,'\n')
arr1=np.vsplit(arr2,2) # split vertically arr2 into 2 equal parts
print(arr1)

