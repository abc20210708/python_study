## 회의실 예약 다른 풀이
# 참고 블로그 https://jie0025.tistory.com/434

import sys
input = sys.stdin.readline



def chkTime(times):
    avail = []
    check = 9
    
    for time in times:
        start, end = time[0], time[1]
        if (check < start):
            avail.append([check, start])
        check = end
        
    if (check != 18):
        avail.append([check, 18])
        
    length = len(avail)
    if (length == 0):
        print("Not available")
    else:
        print(length, "available:")
        for start, end in avail:
            if (start == 9) : start = "09"
            print(str(start) + "-" + str(end))
        
        
        
n, m = map(int, input().split())
res = dict()           

for _ in range(n):
    room = input().rstrip()
    res[room] = []

for _ in range(m):
    room, start, end = map(str, input().split())
    res[room].append([int(start), int(end)])
    
for room, times in sorted(res.items()):
    times.sort(key=lambda x:x[0])
    
    print("Room " + room + ":")
    chkTime(times)
    
    n -= 1
    if (n != 0):
        print("-----")
