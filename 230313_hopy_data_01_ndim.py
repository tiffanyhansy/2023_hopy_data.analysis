'''
p16
ndarray.ndim : array의 차원 알려줌 
ndarray 자리에 array 넣기
'''

import numpy as np

array1 = np.array([[1,2,3]]) #[] 각각 차원이라고 보면 됨
array2 = np.array([1,2,3])

print('array1의 차원 :', array1.ndim)
print('array2의 차원 :', array2.ndim)
