## 비슷한 단어 (실버 2)
#  참고한 코드 https://www.acmicpc.net/source/56021724
import sys
input = sys.stdin.readline

n = int(input())

arr = list(input().rstrip())
result = 0

for i in range(n - 1):
    copy_arr = arr[:]
    temp = list(input().rstrip())
    cnt = 0

    for t in temp:
        if t in copy_arr:
            copy_arr.remove(t)
        else:
            cnt += 1

    if len(copy_arr) <= 1 and cnt <= 1:
        result += 1

print(result)
