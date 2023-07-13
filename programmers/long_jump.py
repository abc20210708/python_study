## 멀리 뛰기

# 3일 때 3가지 방법
# 4일 때 5가지 방법

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
'''

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