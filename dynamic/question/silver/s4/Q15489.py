## 파스칼 삼각형 (실버 4)

# 다른 풀이
# 참고 블로그 https://justduke.tistory.com/m/175
t = [[0 for _ in range(31)] for _ in range(31)]
t[1][1] = 1
for i in range(2,31):
    for j in range(1,31):
        t[i][j] = t[i-1][j-1] + t[i-1][j]
r,c,w = map(int, input().split())
answer = 0
for i in range(w):
    for j in range(i+1):
        answer += t[r+i][c+j]
print(answer)


# 기존 풀이
dp = [[] for _ in range(32)]

for i in range(32):
    for j in range(i+1):
        if i == 0 or j == 0 or j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])
            
r, c, w = map(int, input().split())
tmp = dp[r-1][c-1]

#print(dp)

for i in range(r, r+w-1): #  참고 블로그 https://changsroad.tistory.com/141
    for j in range(c-1, c-1+i-r+2): # i-2로 적용했음
                                    # c-1+i-r+2 
        #print({i},{j})
        #print(dp[i][j])
        tmp += dp[i][j]
        
print(tmp)

## 다른 풀이
#  참고 블로그 https://airzinc.tistory.com/entry/%EB%B0%B1%EC%A4%80-15489-%ED%8C%8C%EC%8A%A4%EC%B9%BC-%EC%82%BC%EA%B0%81%ED%98%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC
tmp, cnt = 0, 0
for i in range(r-1, r+w-1):
    for j in range(c-1, c + cnt):
        tmp += dp[i][j]
    cnt += 1
        
print(tmp)



## 다른 풀이
import math
r, c, w = map(int,input().split())
n = 0
for i in range(r, r+w):
    for j in range(c, c+i-r+1):
        n += math.comb(i-1, j-1)
print(n)