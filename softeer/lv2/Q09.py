# 회의실 예약

# 참고 블로그https://velog.io/@yibangwon/Softeer-21%EB%85%84-%EC%9E%AC%EC%A7%81%EC%9E%90-%EB%8C%80%ED%9A%8C-%EC%98%88%EC%84%A0-%ED%9A%8C%EC%9D%98%EC%8B%A4-%EC%98%88%EC%95%BD-%EB%82%9C%EC%9D%B4%EB%8F%842

import sys

#N, M = map(int, sys.stdin.readline().split())
N, M = 3, 2
#rooms = [] #방 이름을 정렬하기 위해 dictionary가 아닌 list로 선언
rooms = []
status = [[False for i in range(9)] for i in range(50)]

for i in range(N):
    rooms.append(input()) 
rooms.sort()

for i in range(M):
    r, s, e = input().split()
    s, e = int(s) - 9, int(e) - 9
    for j in range(s, e):
        status[rooms.index(r)][j] = True #해당 시간이 사용중
        


for i in range(N):
    print('Room %s:' % rooms[i])
    if False not in status[i]: #빈 시간이 없으면
        print('Not available')
    else:
        k = 0
        available = []
        while k < 9:
            f, t = 0, 0
            if not status[i][k]:
                f = k
                while k < 9 and not status[i][k]:
                    k += 1
                t = k - 1
                available.append([f, t]) #사용 중인 시간을 list에 추가
            k += 1
        print(len(available), 'available:')
        for o in available:
            print('{}-{}'.format(format(o[0] + 9, '02'), format(o[1] + 10, '02')))
    if i != N - 1:
        print('-----')