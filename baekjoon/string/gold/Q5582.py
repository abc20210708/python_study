## 공통 부분 문자열 (골드 5) *

# 참고 블로그 https://fre2-dom.tistory.com/490
# PyPy3으로 제출 

import sys

s1 = list(map(str, sys.stdin.readline().strip()))
s2 = list(map(str, sys.stdin.readline().strip()))

dp = [[0] * (len(s2) + 1) for _ in range(len(s1)+1)]
res = 0

# 반복문으로 두 개의 문자열 확인
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        # 두 개의 문자열 중에 문자가 같다면 dp에 +1로 저장
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            res = max(dp[i][j], res)

print(res)