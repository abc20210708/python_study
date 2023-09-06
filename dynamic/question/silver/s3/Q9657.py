## 돌 게임 3 (실버 3)
#  참고 블로그 https://dev-scratch.tistory.com/96

n = int(input())

tmp = ["SK", "CY"]

# 돌의 개수별로 승자를 저장하는 리스트, 초기값은 모두 -1로 설정.
d = [-1] * 1001

# 초기 상태에서 몇 개의 돌이 있을 때 어떤 플레이어가 이기는지 미리 설정
d[1] = 0  # 1개의 돌이 있을 때는 "SK"가 승리
d[2] = 1  # 2개의 돌이 있을 때는 "CY"가 승리
d[3] = 0  # 3개의 돌이 있을 때는 "SK"가 승리
d[4] = 0  # 4개의 돌이 있을 때는 "SK"가 승리

# 돌의 개수가 5부터 입력받은 개수 n까지 순서대로 승자를 결정
for i in range(5, n + 1):
    # 이전 상태에서 승자가 "SK"이고, i-3, i-4, i-1개의 
    # 돌 상태에서도 "SK"가 승리한다면,
    # 현재 상태에서는 "CY"가 승리
    # 그렇지 않으면 "SK"가 승리
    if d[i - 1] == d[i - 3] == d[i - 4] == 0:
        d[i] = 1
    else:
        d[i] = 0

print(tmp[d[n]])

## 다른 풀이
#  참고 블로그 https://steady-coding.tistory.com/168
N = int(input())

if N % 7 == 0 or N % 7 == 2:
    print("CY")
else:
    print("SK")