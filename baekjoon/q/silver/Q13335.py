## 트럭 (실버 1)
#  참고 블로그 https://ywtechit.tistory.com/187

import sys
input = sys.stdin.readline

# n 다리 건너는 트럭 수, length 다리 길이, w 다리 최대하중
n, length, w = map(int, input().split())
lst = list(map(int, input().split()))
cnt, tmp = 0, 0
bridge = [0] * length

while 1:
    out = bridge.pop(0)
    tmp -= out
    
    if lst:
        if tmp + lst[0] <= w:
            bridge.append(lst[0])
            tmp += lst[0]
            lst.pop(0)
        else:
            bridge.append(0)
    cnt += 1
    
    if not bridge:
        break
    
print(cnt)