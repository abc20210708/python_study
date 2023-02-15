# 8단 변속기

import sys

d = list(int, sys.stdin.readline().split())

asc = d.copy()
asc.sort()

desc = d.copy()
desc.sort(reverse=True)

if d == asc:
    print("ascending")
elif d == desc:
    print("descending")
else:
    print("mixed")
    

'''
참고 블로그 https://dev-note-97.tistory.com/14

✔ sort(reverse = True), sorted(reverse = True) / reverse(), reversed() 차이
reverse = true 옵션을 사용한 sort 와 sorted는 
오름차순 정렬 후 역순, 즉 "내림차순" 으로 정렬되는 것이고,

reverse() 와 reversed() 는 
정렬 과정 없이 순수 배열을 반대로 뒤집는 것입니다.

'''