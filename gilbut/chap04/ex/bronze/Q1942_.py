## 디지털시계 (브론즈 2) *

for _ in range(3):
    start, end = input().split()

    h1, m1, s1 = map(int, start.split(":"))
    h2, m2, s2 = map(int, end.split(":"))
    
    res = 0
    while 1:
        if s1 == 60: m1 += 1; s1 = 0
        if m1 == 60: h1 += 1; m1 = 0
        if h1 == 24: h1 = 0
        
        x  = h1 * 10000 + m1 * 100 + s1
        if x % 3 == 0 : res += 1
        
        if (h1 == h2) and (m1 == m2) and (s1 == s2): break
        s1 += 1
        
    print(res)

# 참고 블로그 http://cobinding.tistory.com/81

'''
# 참고 블로그 https://kau-algorithm.tistory.com/929
import datetime

for i in range(3):
    str, end = input().split()
    start_time = datetime.datetime.strptime(str, "%H:%M:%S")
    interval = datetime.datetime.strptime(end, "%H:%M:%S") - start_time
    
    cnt = 0
    for num in range(0, interval.seconds + 1):
        tmp_time = start_time + datetime.timedelta(seconds=num)
        tmp = tmp_time.strftime("%H%M%S")
        if int(tmp) % 3 == 0:
            cnt += 1
            
    print(cnt)
'''
