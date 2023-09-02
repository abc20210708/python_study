## 다리 놓기 (실버 5)

# 참고 블로그  https://dmaolon00.tistory.com/entry/%EB%B0%B1%EC%A4%80python-%EB%8B%A4%EB%A6%AC-%EB%86%93%EA%B8%B0-1010-%EC%A1%B0%ED%95%A9
import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(math.comb(m, n))

#  참고 블로그 https://yoonsang-it.tistory.com/33

import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w, e = map(int, input().split())
    bridge = math.factorial(e) // (math.factorial(w) * math.factorial(e-w))
    print(bridge)
    

# e가 w보다 크기 때문에 최대 연결할 수 있는 다리의 개수는 w개이고
# e개의 지역에 w개의 다리를 놓을 수 있는 경우의 수를 구하는 것이기 때문에
# eCw 으로 표현할 수 있고 이는 e! 을 (e-w)!w! 으로 나눈 값이 된다.


# 다른 풀이
# 참고 블로그 https://velog.io/@uoayop/BOJ-1010-%EB%8B%A4%EB%A6%AC-%EB%86%93%EA%B8%B0Python
import sys
input = sys.stdin.readline

# 다리는 겹치면 안된다.
def bridge(n,m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,m+1):
        dp[1][i] = i

    for j in range(2,n+1):
        for k in range(j,m+1):
            for l in range(k,j-1,-1):
                dp[j][k] += dp[j-1][l-1]

    return dp[n][m]

T = int(input().rstrip())
for _ in range(T):          
    n, m = map(int,input().rstrip().rsplit())
    print(bridge(n,m))  