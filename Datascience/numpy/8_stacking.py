import numpy as np
arr1=np.round(np.random.random((4,4))*10)
arr2=np.round(np.random.random((4,4))*10)
arr3=np.round(np.random.random((4,4))*10)

#horizontal stacking  (its like concatenation)
a1=np.hstack((arr1,arr2,arr3))
print(a1)
#vertical stacking
a2=np.vstack((arr1,arr2,arr3))
print(a2)