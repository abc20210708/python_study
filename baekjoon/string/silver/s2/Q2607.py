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


## 다른 풀이
#  참고 블로그 https://alpyrithm.tistory.com/127


n = int(input())
words = [[0 for _ in range(26)] for _ in range(n)]

for i in range(n):
    string = input().rstrip()
    for s in string:
        words[i][ord(s)-ord('A')] += 1

res = 0

for word in words[1:]:
    plus, minus = 0, 0
    for i in range(26):
        if word[i] > words[0][i]:
            plus += (word[i]-words[0][i])
        else:
            minus += (words[0][i]-word[i])
    if plus < 2 and minus < 2:
        res += 1
        
print(res)