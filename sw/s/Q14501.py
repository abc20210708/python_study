## 퇴사 (실버 3)
#  참고 블로그 https://hardenkim.tistory.com/43

def solution():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * n
    
    for i in range(n):
        if i + lst[i][0] <= n : # 퇴사 전에 가능한 상담일 경우
            dp[i] = lst[i][1] # 당일 상담의 금액을 저장
            for j in range(i):
                if j + lst[j][0] <= i : # 이전의 상담이 오늘 전에 가능할 경우
                    dp[i] = max(dp[i], dp[j]+lst[i][1])
                    # (이전의 상담 금액 + 당일의 상담 금액)의 최댓값 선택
    return max(dp)

print(solution())






#  참고 블로그 https://yuna0125.tistory.com/124

N = int(input())

t = []
p = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)


for i in range(N-1, -1, -1): # 뒤에서부터 거꾸로
    if t[i] + i > N: # 상담에 필요한 일수가 퇴사일을 넘어가면
        dp[i] = dp[i+1] # 다음날 값 그대로 가져옴
    
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i]) # 오늘 상담을 안 할 경우와 상담을 할 경우 중 max 값

print(dp[0])