## 집합 (실버 5) *

import sys
arr = set()

for _ in range(int(input())):
    temp = sys.stdin.readline().split()
    
    if len(temp) == 1:
        if temp[0] == 'all':
            arr = set([i for i in range(1,21)])
        else:
            arr = set()
    else:
        s, n = temp[0], temp[1]
        n = int(n)

        if s == 'add':
            arr.add(n)
        elif s == 'remove':
            arr.discard(n)
        elif s == 'check':
            print(1 if n in arr else 0)
        elif s == 'toggle':
            if n in arr:
                arr.discard(n)
            else:
                arr.add(n)