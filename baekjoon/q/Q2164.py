# 카드 2
## 참고 블로그 https://tooo1.tistory.com/88
num = int(input())
cnt = 2

while 1:
    if (num == 1 or num == 2):
        print(num)
        break
    cnt *= 2
    if (cnt >= num):
        print((num - (cnt // 2)) * 2)
        break


'''
from collections import deque
num = int(input())

q = deque([i for i in range(1, num+1)])

while len(q) != 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)
    
print(q[0])
'''