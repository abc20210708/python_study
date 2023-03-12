# 카드 2
from collections import deque
num = int(input())

q = deque([i for i in range(1, num+1)])

while len(q) != 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)
    
print(q[0])