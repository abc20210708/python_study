## 도로와 신호등 (실버 4)
#  참고 블로그 https://velog.io/@bjo6300/%EB%B0%B1%EC%A4%80-2980-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8F%84%EB%A1%9C%EC%99%80-%EC%8B%A0%ED%98%B8%EB%93%B1

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pos = 0 # 현재 위치
res = 0

for _ in range(n):
    d, r , g = map(int, input().split())
    
    res += (d - pos) # 신호등 위치 - 현재 위치
    pos = d # 현재 위치 갱신
    
    if res % (r + g) <= r: # 경과시간 % (빨간불 + 초록불)이
                            # 빨간불 이하면 대기
        res += (r - (res % (r + g)))
    
res += (l-pos)# 반복문을 돌고나면 신호등이 없는 도로 길이 더해야함
print(res)