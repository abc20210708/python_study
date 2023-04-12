a = [1, 2, 3, 4, 5]
print(a[0:2])
'''
## 참고 블로그 https://blog.naver.com/kut_da_92/222687098324

# List.index(value)

item이 갖는 값이 인자 값으로 들어오는 value값과 같은
첫 번째 index를 return 합니다.

만약에 value에 해당하는 값이 없는 경우에는 
ValueError가 발생합니다.
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.index('banana'))

# 4번 인덱스로부터 banana라는 값을 가진 item의
# 첫 번째 인덱스는 6
print(fruits.index('banana', 4))
