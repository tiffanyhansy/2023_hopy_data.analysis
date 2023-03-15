'''
p18
astype() ndarray 내 데이터 타입 변경
astype()의 인자에 원하는 타입을 문자열로 지정
'''

import numpy as np

array_int = np.array([1,2,3])
array_float = array_int.astype('float64')   #데이터 타입 int32 -> float64
print(array_float, array_float.dtype)   #array_float의 데이터 타입 출력

array_int1 = array_float.astype('int32')    #데이터 타입 float64 -> int32
print(array_int1, array_int1.dtype)     #array_int1 의 데이터 타입 출력

array_float1 = np.array([1.1,2.1, 3.1])
array_int2 = array_float1.astype('int32')   #데이터 타입 int32
print(array_int2, array_int2.dtype)
