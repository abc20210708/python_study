## 한 줄로 서기 (실버 2)
#  참고 블로그 https://fre2-dom.tistory.com/400

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
res = [0] * n

# 반복문을 통해 각 자리에 들어갈 사람을 확인
for i in range(n):
    cnt = 0 # 자신의 왼쪽의 키 큰 사람 수
    # 반복문을 통해 모든 사람을 확인
    for j in range(n):
        # 자신의 왼쪽 키 큰 살마의 수가 맞고 그 자리에 아무도 없다면
        if cnt == lst[i] and res[j] == 0:
            res[j] = i + 1
            break
        # 자리에 아무도 없다면 자신의 왼쪽 키 큰 사람 수 카운트
        elif res[j] == 0:
            cnt += 1
            
print(*res)
# print(' '.join(map(str, res)))