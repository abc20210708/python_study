## 프린터 큐 (실버 3)
from collections import deque

# 참고 블로그 https://hei-jayden.tistory.com/209
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque(list(range(N)))
    cnt = 0

    # 최종적으로 M이 제거될 때까지 while문 반복
    while M in idx:

        # 0번 째 인덱스에 q의 가장 큰 값이 위치하도록 조정
        while max(q) != q[0]:
            q.append(q.popleft())
            idx.append(idx.popleft())

        # 조정이 완료되었을 때, 0번 째 인덱스 값 제거하면서 cnt+1
        cnt += 1 
        q.popleft()
        idx.popleft()

    # M이 제거되었을 때 cnt 값 확인
    print(cnt)

# 참고 블로그 https://dndi117.tistory.com/14
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    que = deque(list(map(int, input().split())))
    idx_que = deque(list(range(n)))
    cnt = 0
    
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx_que.popleft() == x:
                print(cnt)
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())


#  duque 이용한 다른 풀이
#  참고 블로그 https://hongcoding.tistory.com/42


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    d = deque(list(map(int, input().split())))
    res = 0
    
    while d:
        best = max(d) # 현재의 최댓값이 가장 먼저 배출되므로
                        # 최댓값을 저장
        front = d.popleft() # 큐의 front를 뽑았으므로 
        m -= 1 # 내 위치가 한 탕 당겨짐
        
        if best == front: # 뽑은 숫자가 제일 큰 숫자인 경우
            res += 1
            if m < 0 : # m이 0이라는 것은 뽑은 숫자가 내 숫자
                print(res)
                break
        else: # 뽑은 숫자가 제일 큰 숫자가 아닌 경우
            d.append(front) # 제일 뒤로
            if m < 0: # 제일 앞에서 뽑히면
                m = len(d) - 1 # 제일 뒤로 이동
            
        
        
    
    


n = int(input())
for i in range(n):
    m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    while len(arr) > 0:
        if arr[0] == max(arr):
            cnt += 1
            arr.pop(0)
            if k == 0: break
        else:
            arr.append(arr.pop(0))
        k = k - 1 if k > 0 else len(arr) -1
    print(cnt)
            

        
    