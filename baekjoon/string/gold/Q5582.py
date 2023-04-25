## 공통 부분 문자열 (골드 5) *

# 참고 블로그 https://fre2-dom.tistory.com/490
# PyPy3으로 제출 

import sys

s1 = list(map(str, sys.stdin.readline().strip()))
s2 = list(map(str, sys.stdin.readline().strip()))

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
answer = 0

# 반복문을 통해 두 개의 문자열을 확인
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        # 두 개의 문자열중에 문자가 같다면 dp에 +1로 저장
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)

print(answer)


## 다른 풀이
import sys
def input(): return sys.stdin.readline().rstrip()

str1, str2 = input(), input()
subs = [[0] * len(str2) for _ in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            subs[i][j] = 1 
            if i-1 >= 0 and j-1 >= 0:
                subs[i][j] += subs[i-1][j-1]
            
print(max([max(arr) for arr in subs]))