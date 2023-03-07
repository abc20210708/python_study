
# 대회 or 인턴
# 참고 블로그 https://jeongminhee99.tistory.com/65


##n, m, k = 6, 3, 2

'''
team = 0

while True:
    
    n -= 2
    m -= 1
    
    if n < 0 or m < 0 or (n + m) < k:
        break
    
    team += 1
    
print(team)
'''  



# 6 10 3
n, m, k = map(int, input().split())

result = 0

while n >= 2 and m >= 1 and n + m >= k + 3 :
    #2명, 1명 팀 만들 수 있고, 인텁쉽도 보낼 수 있는 경우
    n -= 2
    m -= 1
    result += 1 #팀 수는 더해주기
    
print(result)

