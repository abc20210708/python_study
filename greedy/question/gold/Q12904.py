# A와 B (골드 5) *

# 참고 블로그 https://chocochip101.tistory.com/entry/%EB%B0%B1%EC%A4%80-12904%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-A%EC%99%80-B

import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())


'''
1. 문자열 뒤에 A를 추가
2. 문자열을 뒤집고, 뒤에 B를 추가
'''

chk = False
while t:
    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t.reverse()
    if s == t:
        chk = True
        break
    
print(1) if chk else print(0)