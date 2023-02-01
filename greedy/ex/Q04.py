# 만들 수 없는 금액

# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값

 n = int(input())
 c = list(map(int, input().split()))
#c = [1, 2, 3, 8]
c.sort()

# 처음에는 금액 1을 만들 수 있는지 확인하기 위해
# target을 1로 설정
target = 1
for x in c:
   # 만들 수 없는 금액을 찾았을 때 반복 종료
   if target < x:
       break
   target += x
   
# 만들 수 없는 금액 출력
print(target)
    