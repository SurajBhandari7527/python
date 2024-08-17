import numpy as np
def whatever(array):
    return np.sin(array)
array=np.random.randint(1,20,10)
arr=whatever(array)
print(arr)