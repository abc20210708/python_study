## 다이나믹이 뭐예요? (실버 3)  


# 참고 블로그 https://coooco.tistory.com/60
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#n, m 행렬 이므로 모두 다 1로 초기화
array =[[1]* n for _ in range(m)]
 
for i in range(1,m):
    for j in range(1,n):
        array[i][j]=(array[i-1][j-1]+array[i-1][j]+array[i][j-1])%1000000007
 
print(array[m-1][n-1])