## 미아 노트 (실버 5) *

# 참고 블로그 https://dreamtreeits.tistory.com/147
import sys

n, h, w = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(h)]

def solution(x):
    global res
    for i in range(x * w, (x + 1) * w):
        for j in range(h):
            if arr[j][i] != "?":
                res += arr[j][i]
                return
    res += "?"
    return


res = ""
for i in range(n):
    solution(i)
print(res)