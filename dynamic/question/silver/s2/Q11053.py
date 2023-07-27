## 가장 긴 증가하는 부분 수열 (실버 2)
#  참고 블로그 https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-11053.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-by-Python
#  https://duckracoon.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%95%B4%EC%84%A4-python

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))