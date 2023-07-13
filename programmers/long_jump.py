## 멀리 뛰기

# 3일 때 3가지 방법
# 4일 때 5가지 방법

# 참고 블로그 https://velog.io/@wjdtmdgml/프로그래머스멀리뛰기12914번Python파이썬DP

def solution(n):
    if n < 3:
        return n
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = d[i-1] + d[i-2]
    return d[n] % 1234567


''' 
1. 피보나치 응용으로 생각 (런타임 에러)
  원래 피보나치는 1:1, 2:1, 3:2, 4:3

memory = {1:1, 2:2}

def solution(n):
    if n in memory:
        num = memory[n]
    else:
        num = solution(n-1) + solution(n-2)
        memory[n] = num
    return num % 1234567
    
    
프로그래머스 다른 풀이 (izjoker님 코드 참고)

import sys
sys.setrecursionlimit(10**6) # 재귀 호출의 최대 깊이 설정 코드

memory = {1: 1, 2:2, 3:3, 4:5}

def solution(n):
    if n in memory:
        return memory[n]
    memory[n] = (solution(n-2) + solution(n-1)) % 1234567
    return memory[n] 



'''