# 약수 구하기

# N의 약수들 중 K번째로 작은 수를 출력

n, k = map(int, input().split())

arr = [i for i in range(1, n+1) if n%i == 0]

# k 값이 배열의 크기보다 큰 경우 0 출력
if k > len(arr):
    print(0)
else:
    print(arr[k-1])