## 뒤집기 (실버 5) *

import sys

## 다른 풀이
# 참고 블로그 https://eunhee-programming.tistory.com/296

string = str(sys.stdin.readline().strip())

arr_0 = string.split("1")
arr_1 = string.split("0")

res_0 = 0
res_1 = 0

for i in arr_0:
    if "0" in i:
        res_1 += 1
        
for i in arr_1:
    if "1" in i:
        res_0 += 1
        
print(min(res_1,res_0))


#

s = list(map(int, sys.stdin.readline().strip()))

cnt = 0
# 반복문을 통해 문자열을 확인
for i in range(len(s) -1):
    # 현재 문자와 다음 문자가 다르면 카운트
    if s[i] != s[i+1]:
        cnt += 1

# cnt + 1을 2로 나눈 나머지를 출력
print((cnt + 1)//2)