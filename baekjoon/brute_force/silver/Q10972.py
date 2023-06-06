## 다음 순열 (실버 3) *
# 참고 블로그 https://velog.io/@wlrhkd49/%EB%B0%B1%EC%A4%80-10972-%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-Python

n = int(input())
data = list(map(int, input().split()))

for i in range(n-1, 0, -1): # 맨 뒤 값부터 시작
    if data[i-1] < data[i]:
        for j in range(n-1, 0, -1): # 다시 맨 뒤 값부터 큰 값찾기
            if data[i-1] < data[j]:
                data[i-1], data[j] = data[j], data[i-1] # 둘 값을 swap
                data = data[:i] + sorted(data[i:])
                for i in data:
                    print(i, end=' ')
                exit()
print(-1)
        
# 1 4 3 2 를 예시

'''

 1. 뒤부터 순열을 비교해, 뒷 값이 앞 값보다 큰 경우까지 반복
 (3, 2), (4, 3)은 해당하지 않고 (1, 4)는 해당
 이 때, 1의 인덱스는 x, 4의 인덱스는 y라고 한다.
 
 2. 다시 뒤부터 값을 비교해 인덱스 x보다 큰 값이 있으면
 그 값과 swqp, 1과 2를 비교했고, 2가 크기 대문에 이 둘을 swap
 
 3. y에 해당하는 인덱스부터 오름차순 정렬을 한 뒤에 이어 붙인다.
  4 3 1 sort해서 1 3 4가 된다. 이어 붙여 2 1 3 4
  
'''