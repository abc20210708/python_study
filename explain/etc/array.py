## 참고 블로그 https://covenant.tistory.com/142

# 4-1. 배열 초기화

'''
3 5
두 정수가 첫째 줄에 입력값으로 들어옵니다.
첫 번재 정수는 배열의 가로 크기를, 두 번째 정수는
배열의 세로 크기인 0으로 초기화된 배열을 만들어 봅시다.
위의 입력값은 가로 3 세로 5인 크기의 배열을 0응로 초기화
'''

N, M = map(int, input().split())
arr = [[0] * N for _ in range(M)]

'''
가로를 N, 세로를 M
'''

# 4-2 배열의 원소를 거꾸로
arr.reverse() # 반환 값이 없음

'''
472
385
'''

# 입력
A = int(input())
B = int(input())

# B의 값을 문자열로 변환한 다음에 앞에서 한 글자씩
# 배열에 넣는 코드
arr_B = [int(i) for i in str(B)]

'''
arr = list(map(int, list(String)))  
arr = [int(i) for i in String]
두 코드 모두 arr에 [1, 2, 3]이 저장됩니다.
'''

arr_B.reverse()

for i in range(len(arr_B)):
    print(A * arr_B[i])
print(A * B)


# 4-3 배열 원소의 갯수
# list.count(찾는 값) # 값이 배열에 몇 개가 있는지 찾으려면
# str.count(찾는 값)  # 문자열도 가능

# 4-4 원소 중복 제거
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ] 
alpha = list(set(alpha))

# 2차원 리스트가 있습니다. 중복된 값을 제거하려면 어떻게 해야할까요?
lst = [[1,2], [1,2], [1]] 
print(list(set(map(tuple, lst))))


# 4-5 배열 정렬
arr.sort() # 오름차순
arr.sort(reverse=True) # 내림차순

# 배열의 원소가 한 개가 아닌 리스트라면
arr.sort(key=lambda x:(x[0], x[1]))
# arr.sort(key=lambda x:(x[0], x[1])) 를 이용해서
# x[0] (x좌표)을 정렬하고, x[0] 값이 같다면 x[1] (y좌표)을 기준으로 
# 오름차순 정렬합니다.

'''
그렇다면 내림차순 정렬을 하는 방법은 무엇일까요?
-x[0] 이렇게 -를 붙이면 됩니다. 
이 방법을 이용하면 백준 10825번 
국영수 문제를 해결할 수 있습니다.

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
'''

# 파이썬 삼항 연산자
# [True 조건] if 조건 else [False 조건]

# a와 b 중에서 큰 값을 result에 저장한다고 하면
'''
if a > b:
    res = a
else:
    res = b
'''

a = 7
b = 9

res = a if a > b else b
print(res)