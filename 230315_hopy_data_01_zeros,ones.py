'''
p19

zeros() 함수 인자는 shape 값을 입력하면 모든 값을 0으로 채운 후 해당 shape를 가진 ndarray를 반환
ones() '' 1로 채운 후 반환
함수 인자로 dtype를 정해주지 않으면 default로 float6로 ndarray 채움
'''

import numpy as np

zero_array = np.zeros((3,2), dtype = 'int32')   #(3,2) : shape, 'int32'로 data type 정해줌
print(zero_array)
print(zero_array.dtype, zero_array.shape)

one_array = np.ones((3,2))  #data type 미정, default인 float64로 출력 예상?
print(one_array)
print(one_array.dtype, one_array.shape)
