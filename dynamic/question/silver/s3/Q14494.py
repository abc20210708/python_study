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

'''
1. array =[[1]* n for _ in range(m)]
2. array =[[1]* n] * m  차이점

1. 코드를 실행하면 각 행이 별도로 생성되고, 각 행은 n개의 1로 채워집니다. 
따라서 각 행은 독립적입니다. 
즉, 하나의 행을 수정하더라도 다른 행에 영향을 미치지 않습니다.

2.
하나의 행을 만들고 이 행을 m번 복제하여 리스트를 생성합니다. 
그러나 모든 행은 동일한 행 객체를 가리킵니다. 
따라서 하나의 행을 수정하면 나머지 행도 동일하게 수정됩니다.

요약하면, 첫 번째 코드는 각 행이 독립적으로 생성되고 수정되지만, 
두 번째 코드는 모든 행이 동일한 행 객체를 참조하므로 하나를 수정하면 모두 변경됩니다.
'''