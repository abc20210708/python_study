## 카드 숫자 곱의 경우의 수 (실버 3) *
# 참고 블로그 https://readble-ko.tistory.com/137

N = int(input())
checker = [False] * 5000000
answer = 0

arr = [1]
checker[1] = True

for _ in range(N):
    size = len(arr)
    for j in range(size):
        for k in range(1, 10):
            tmp = arr[j] * k
            if not checker[tmp]:
                checker[tmp] = True
                arr.append(tmp)

print(len(arr))