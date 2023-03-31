## 디지털시계 (브론즈 2) *

# 참고 블로그 https://kau-algorithm.tistory.com/929
import datetime

for i in range(3):
    start, end = input().split()
    start_time = datetime.datetime.strptime(start, "%H:%M:%S")
    interval = datetime.datetime.strptime(end, "%H:%M:%S") - start_time
    
    cnt = 0
    for num in range(0, interval.seconds + 1):
        tmp_time = start_time + datetime.timedelta(seconds=num)
        tmp = tmp_time.strftime("%H%M%S")
        if int(tmp) % 3 == 0:
            cnt += 1
            
    print(cnt)
    
