## 애너그램 만들기 (브론즈 2)
#  참고 블로그 https://velog.io/@ddochi132/BOJ-1919%EB%B2%88-%EC%95%A0%EB%84%88%EA%B7%B8%EB%9E%A8-%EB%A7%8C%EB%93%A4%EA%B8%B0-PYTHON
import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

for s in s1:
    if s in s2:
        s1 = s1.replace(s, '',1)
        s2 = s2.replace(s, '',1)
# (s, '', 1)       
# 뒤에 1은 치환횟수인데 1을 넣지 않으면 aab , a 일 때 b만 남게 됨
print(len(s1)+len(s2))
