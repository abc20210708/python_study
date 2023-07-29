## 가장 큰 증가하는 부분 수열 (실버 2)
#  참고 블로그 https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11055-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A6%9D%EA%B0%80-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4
import sys
input = sys.stdin.readline

# 참고 블로그 https://cotak.tistory.com/46
# 리스트 복사 참고 https://inkkim.github.io/python/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B3%B5%EC%82%AC/
# dp = a[:] 리스트를 다른 리스트에 복사하는 방법
# 시작점과 끝점을 생략한 슬라이싱은 리스트의 모든 요소를 뜻한다.
# 슬라이싱을 통해 변수를 정의하면 파이썬은 새로운 객체를 만든다.

n = int(input().strip())
a = list(map(int, input().split()))
dp = a[:]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))




n = int(input())
nums = list(map(int, input().split()))

d = [1] * n
d[0] = nums[0]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            d[i] = max(d[i], d[j]+nums[i])
        else:
            d[i] = max(d[i], nums[i])

print(max(d))

'''

1. 해당 값보다 작은 값을 더한 후 가장 큰 값 출력으로 시도 - 틀림

n = 10
nums = [1,100,2,50,60,3,5,6,7,8]

res = [] 

for i in range(1, n):
    tmp = 0
    for j in range(i):
        if nums[i] > nums[j]:
            tmp += nums[j]
    tmp += nums[i]
    res.append(tmp)
            
            
print(max(res))
'''

