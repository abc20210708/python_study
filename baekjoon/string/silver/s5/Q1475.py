## 방 번호 (실버 5) *

# 참고 블로그 https://bgspro.tistory.com/62
import sys
input = sys.stdin.readline().rstrip

s = input()

res = [0] * 10

for i in range(len(s)):
    num = int(s[i])
    if num == 6 or num == 9:
        if res[6] <= res[9]:
            res[6] += 1
        else:
            res[9] += 1
    else:
        res[num] += 1
        
print(max(res))