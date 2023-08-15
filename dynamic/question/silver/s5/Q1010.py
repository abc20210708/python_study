## 다리 놓기 (실버 5)
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