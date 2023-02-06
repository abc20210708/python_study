# 두 배열의 원소 교체


n, cnt = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # 배열 A는 오름차순 정렬 수행
B.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번재 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(cnt):
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        # 두 원소를 교체
        A[i], B[i] = B[i], A[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
        break
    
print(sum(A))
        
    

