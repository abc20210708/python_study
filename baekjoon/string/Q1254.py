# 팰린드롬 만들기

## 참고 블로그 https://velog.io/@sugenius77/%EB%B0%B1%EC%A4%80Python-1254%EB%B2%88-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0

import sys
s = sys.stdin.readline().strip()

for i in range(len(s)):
    print(s[i:][::-1])
    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break