'''
p17
ndarray.dtype 을 통해 데이터 타입 (data type) 을 알 수 있다
ndarray 자리에 array 넣기
'''

import numpy as np

#같은 데이터 타입일 때

list1 = [1,2,3]
print(type(list1))  

array1 = np.array(list1)    #.array 함수를 이용해 list1을 넘파이 기반 데이터 타입인 ndarray로 변환
print(type(array1))
print(array1, array1.dtype)


#다른 데이터 타입일 때 -> 데이터 타입이 더 큰 데이터로 변환됨

list2 = [1,2, 'test']   #'test'라는 string 형 -> 1,2가 유니코드 문자열로
array2 = np.array(list2)
print(array2, array2.dtype)

list3 = [1,2,3.0]   #3.0이라는 float 형 -> 1,2가 float64 형으로
array3 = np.array(list3)
print(array3, array3.dtype)
