a = [1, 2, 3, 4, 5]
print(a[0:2])
'''

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

## 문자열을 원소로 가진 리스트에서 특정 인덱스를 기준으로 정렬
# 문자열의 마지막 글자를 기준으로 오름차순 정렬하기
f = ["apple", "banana", "mango", "blueberry"]
f = sorted(f, key=lambda x:x[-1])
print(f)


# 리스트를 원소로 가진 리스트를 길이순으로 정렬
lst = [[0,13,2], [5], [4,3,2,1]]
lst2 = sorted(lst, key=lambda x:len(x))
print(lst2) # [[5], [0, 13, 2], [4, 3, 2, 1]]

res = list(filter(lambda x:x > 0, [1, -3, 2, 0, -5, 6]))
print(res) # [1, 2, 6]

## map(f, iterable)은 함수(f)와 반복가능한 자료형을 입력으로 받는다.
#  map은 입력받은 자료형의 각 요소가 함수 f가 수행한 결과를 묶어서 돌려주는 함수
arr = list(map(lambda a:a*2, [1, 2, 3, 4])) 
print(arr) #[2, 4, 6, 8]

## pow(x, y)는 x의 y제곱한 결괏값을 돌려주는 함수
print(pow(2, 4)) # 16

## zip(iterable)은 동일한 개수로 이루어진 자료형을 묶어주는 역할
tmp = list(zip([1,2,3], [4,5,6], [7,8,9]))
print(tmp) # [(1,4,7), (2,5,8), (3,6,9)]
tmp2 = list(zip("abc", "def"))
print(tmp2)
#[('a', 'd'), ('b', 'e'), ('c', 'f')]

## 참고 블로그 https://blog.naver.com/kut_da_92/222687098324
#  https://hyonlog.tistory.com/2
#  https://velog.io/@winckey0/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%ED%85%8C-%ED%95%A8%EC%88%98-%EA%B3%84%EC%82%B0
