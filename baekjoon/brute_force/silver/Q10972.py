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
        