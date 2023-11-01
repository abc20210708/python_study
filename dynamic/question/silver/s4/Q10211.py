## Maximum Subarray (실버 4)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)):
        tmp[i] = max(tmp[i], tmp[i] + tmp[i-1])
    print(max(tmp))