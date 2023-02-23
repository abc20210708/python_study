# 쉽게 푸는 문제

## 참고 블로그 https://velog.io/@boyfromthewell/%EB%B0%B1%EC%A4%80-1292%EB%B2%88-%EC%89%BD%EA%B2%8C-%ED%91%B8%EB%8A%94-%EB%AC%B8%EC%A0%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
val = 0
arr = [0]

for i in range(1, m + 1):
    for j in range(i):
        arr.append(i)
        
for i in range(n, m + 1):
    val += arr[i]
    
print(val)

'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

arr = [0]

for i in range(1, b + 1):
    for j in range(i):
        arr.append(i)
        
temp = arr[a : b+1]
print(sum(temp))
print(sum(temp))
'''