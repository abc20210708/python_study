## 점심 식사시간
#  참고 블로그 https://hyunse0.tistory.com/394

from itertools import combinations
from collections import deque

# 두 그룹으로 나누어 내려가는 시간 계산
def go_for_lunch(people, stairs):
    # 계단까지 도착하는 시간
    st = []
    
    for p in people:
        st.append(abs(p[0]-stairs[0])+abs(p[1]-stairs[1]))
        
    st = deque(sorted(st))
    
    # 계단을 내려가서 도착할 시간
    e = deque()
    
    time = 0
    now = 0
    
    while st:
        time += 1
        # 이동을 완료한 경우
        while e and e[0] == time:
            e.popleft()
            now -= 1
            
        while st[0] < time:
            # 계단 이동
            if now < 3:
                st.popleft()
                if not st:
                    time += graph[stairs[0]][stairs[1]]
                    break
                e.append(time + graph[stairs[0]][stairs[1]])
                now += 1
            else:
                break
            
    return time



t = int(input())
for t in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    people, stairs = [], []
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                people.append((i, j))
            elif graph[i][j] > 1:
                stairs.append((i, j))
    
    total = int(1e9)
    
    for i in range(n):
        for peo in combinations(people, i):
            tmp = list(set(people)-set(peo))
            time = max(go_for_lunch(peo, stairs[0]), go_for_lunch(tmp, stairs[1]))
            total = min(total, time)
            
    print(f"#{t} {total}")
