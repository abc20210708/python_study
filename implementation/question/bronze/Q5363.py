## 요다 (브론즈 2)

n = int(input())

for _ in range(n):
    s = list(map(str, input().split()))
    print(' '.join(s[2:])+ ' ' + ' '.join(s[:2]))