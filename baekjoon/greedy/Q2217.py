## 로프 (실버 4)

n = int(input())
w = []
res = 0

for i in range(n):
    w.append(int(input()))
    
w.sort()

for i in range(len(w)):
    if w[i] * n > res:
        res = w[i] * n
    n -= 1
    
print(res)

## 다른 풀이
#  참고 코드 https://www.acmicpc.net/source/55728690

#2217 로프
import sys
input=sys.stdin.readline

n=int(input())
lst=[0 for i in range(10001)]
ans=[]
for i in range(n):
    lst[int(input())]+=1

for i in range(len(lst)):
    if lst[i]!=0:
        ans.append(i*n)
        n-=lst[i]

print(max(ans))