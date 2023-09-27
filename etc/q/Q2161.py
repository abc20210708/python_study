## 카드1 (실버 5)

# queue를 사용해 풀이해보기

from collections import deque

n = int(input())
d = deque()

for i in range(1, n+1):
    d.append(i)
    
while len(d) != 1:
    print(d.popleft(), end=" ") # 2, 3, 4
    d.append(d.popleft())
    
print(d[0], end=" ")


# stack 활용 풀이
n = int(input())

d = []

for i in range(1, n+1):
    d.append(i)

while len(d) != 1:
    print(d.pop(0), end=" ") # 2, 3, 4
    d.append(d.pop(0)) # 3, 4, 2

print(d[0], end=" ")
