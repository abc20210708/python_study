## 참고 블로그 https://covenant.tistory.com/143

# deque 

from collections import deque
deq = deque() # 덱 초기화

deq = deque([i for i in range(1, 5)])
# deq에는 [1, 2, 3, 4] 가 저장됩니다.

deq.appendleft(10)
# 왼쪽에 값을 추가하려면 appendleft(value)
# 실행 후 [10, 1, 2, 3, 4]

# 오른쪽에 갑을 추가하려면 append(value)
deq.append(-10)
# 실행 후 [10, 1, 2, 3, 4, -10]

# 오른쪽에서 값을 제거하려면 pop()
# 비어있는 경우는 IndexError: pop from an empty deque
print(deq.pop())

# 왼쪽의 값을 제거하려면 popleft()
# 비어있는 경우는 IndexError: pop from an empty deque
print(deq.popleft())

# 길이 
len(deq)

# rotate 회전하는 방법 
deq.rotate(-1) # 음수이면 왼ㅉ고으로 회전

# 백준 2164 카드2 
N = int(input())
card_queue = deque([i for i in range(1, N + 1)])
while len(card_queue) != 1:
    card_queue.popleft()
    card_queue.rotate(-1)
    
print(card_queue[0])


# 우선순위 큐
from queue import PriorityQueue
que = PriorityQueue()

que.put(4)
que.put(10)  
que.put(2)
 
for i in range(len(que.queue)):  
    print(que.queue[i], end=" ")
    
# 2 10 4 

# 우선순위 큐에 저장된 값은 get()을 이용해 제거
# 제거한 값이 리턴
que.get()


# 실행 시간을 알고 싶을 때
import time 
start_time = int(round(time.time() * 1000)) 
#some_func() 
end_time = int(round(time.time() * 1000)) 
print('some_func()의 실행 시간 : %d(ms)' % (end_time - start_time))
#some_func() 가 실행 시간을 ms 단위로 출력해줍니다.

