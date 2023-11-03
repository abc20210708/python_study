## 타노스 (실버 3)
#  참고 블로그 https://velog.io/@peacemiller/%EB%B0%B1%EC%A4%80-20310-%ED%83%80%EB%85%B8%EC%8A%A4-python

import sys
input = sys.stdin.readline

s = list(input().rstrip())

zero = s.count('0')
one = s.count('1')

# 앞에서부터 1을 갯수의 절반 만큼 지우고
# 뒤에서부터 0을 갯수의 절반 만큼 지우자

cnt = 0
for i in s:
    if cnt == one//2:
        break
    if i == '1':
        s.remove(i)
        cnt += 1


tmp = 0
s = s[::-1]
for i in s:
    if tmp == zero//2:
        break
    if i == '0':
        s.remove(i)
        tmp += 1

for i in s[::-1]:
    print(i, end='')