## JOI와 IOI (브론즈 2)
#  참고 블로그 https://claude-u.tistory.com/426

import sys
input = sys.stdin.readline

s = input().rstrip()

JOI = 0
IOI = 0

for i in range(len(s)-2):
    res = ""
    res += s[i] + s[i+1] + s[i+2]
    
    if res == "JOI":
        JOI += 1
    if res == "IOI":
        IOI += 1
        
print(JOI)
print(IOI)