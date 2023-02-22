# 소수 찾기
## 참고 블로그 https://velog.io/@hrzo1617/%EB%B0%B1%EC%A4%80-1978-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    chk = 0
    if i == 1:
        continue # 1일 때 먼저 예외처리
    for j in range(2, i):
        if i % j == 0: # 나눠지면 1로 변경
            chk = 1    
    if chk == 0:    #반복문 후 상태가 0이면 cnt +1
        cnt += 1
        
print(cnt)