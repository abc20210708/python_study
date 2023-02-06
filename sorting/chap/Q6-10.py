# 위에서 아래로

N = int(input())

array = []
for i in range(N):
    array.append(int(input()))
    
# 파이썬 기본 라이브러리를 이용해 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행되 결과 출력
for i in array:
    print(i, end=' ')
    
    