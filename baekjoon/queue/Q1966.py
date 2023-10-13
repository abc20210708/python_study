## 프린터 큐 (실버 3)

#  duque 이용한 다른 풀이
#  참고 블로그 https://hongcoding.tistory.com/42
from collections import deque

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
            

        
    