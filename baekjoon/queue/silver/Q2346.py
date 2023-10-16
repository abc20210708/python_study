## 풍선 터뜨리기 (실버 3)
#  참고 블로그 https://jobdong7757.tistory.com/117

n = int(input())
s = list(map(int,input().split()))
start = 0
index = [x for x in range(1,n+1)]
res = []
tmp = s.pop(start)
res.append(index.pop(start))

while s:
    if tmp < 0:
        start = (start+tmp) % len(s)
    else:
        start = (start+tmp-1) % len(s)
    tmp = s.pop(start)
    res.append(index.pop(start))
    
for i in res:
    print(i,end=' ')