## 파스칼 삼각형 (실버 4)


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