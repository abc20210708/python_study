## 동전 2 (골드 5)
#  참고 블로그 https://tesseractjh.tistory.com/137
#  https://he-ya.tistory.com/24

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 나올수 있는 가치보다 큰 수가 k + 1개 있는 리스트 생성
dp = [10001] * (k+1)

# 0의 가치는 동전이 필요없음
dp[0] = 0

#  코인 배열의 값을 가져오고
for num in coins:
     # 코인의 가치부터 목표하는 금액까지를 확인하여
    for i in range(num, k+1):
        dp[i] = min(dp[i],dp[i-num]+1)
    # 현재 값에서 가져온 코인 값을 빼주었을 때의 코인 사용 개수에 지금 코인 개수 하나를 더한 값과 
    # 이전 코인들로만 조합했을 때 사용된 코인 개수를 비교하여 더 작은 값을 dp배열에 담기
    
    # 현재 확인하는 코인의 가치만큼 뺐을 때 다른 코인의 조합으로 만들어지지 않으면 10001이
    # 저장되어 있을것이므로 확인하려는 자리 값이 갱신되지 않을 것
if dp[k] == 10001:
   print(-1)
    # 마지막 값이 갱신된 적이 없으면 -1을 출력
else:
   print(dp[-1])
    # 아니라면 마지막 값을 출력