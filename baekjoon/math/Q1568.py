# 새

## 참고 블로그 https://www.acmicpc.net/problem/1568
# 현재 앉아 있는 새의 수
n = int(input())

cnt = 0
k = 1 # 1부터 노래하기 시작

while n > 0 :
    # 만약 불러야하는 음계가 남아있는 새의 수보다 많으면
    if k > n:
        # 음계를 1로 초기화
        k = 1
    # 부른 음계만큼 새의 수가 감소
    n -= k
    # 새를 떠난 뒤 음계를 1씩 올려줌
    k += 1
    cnt += 1
    
print(cnt)
        