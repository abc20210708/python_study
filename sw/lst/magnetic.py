## 특이한 자석
#  참고 블로그 https://swbeginner.tistory.com/entry/SWEA-%EC%BD%94%EB%94%A9-SW-%EB%AA%A8%EC%9D%98%EC%97%AD%EB%9F%89-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%8A%B9%EC%9D%B4%ED%95%9C-%EC%9E%90%EC%84%9D-PYTHON-4013

def dfs(idx, dir):
    
    # 방문 확인
    chk[idx] = 1
    
    # 시계방향으로 움직이면
    if dir == 1:
        # 톱니 바퀴 이동
        wheel[idx].insert(0, wheel[idx].pop(-1))
        
        # 0~3번 톱니이고, 방문한 적 없다면
        if 0 < idx +1 < 4 and chk[idx+1] == 0:
            # 현재 톱니의 3번(이동 전 2번)과 오른쪽 톱니의 6번 확인
            if wheel[idx][3] != wheel[idx+1][6]:
                dfs(idx+1, -1)
        if 0 <= idx -1 < 4 and chk[idx-1] == 0:
            # 현재 톱니의 7번(이동 전 6번)과 왼쪽 톱니의 2번 확인
            if wheel[idx][7] != wheel[idx-1][2]:
                dfs(idx-1, -1)
    else: # 반시계 방향
        # 톱니 바퀴 이동
        wheel[idx].append(wheel[idx].pop(0))
        
        
        if 0 < idx +1 < 4 and chk[idx+1] == 0:
            if wheel[idx][1] != wheel[idx+1][6]:
                dfs(idx+1, 1)
        if 0 <= idx -1 <4 and chk[idx-1] == 0:
            if wheel[idx][5] != wheel[idx-1][2]:
                dfs(idx-1, 1)
    return
        

t = int(input())

for tc in range(1, t+1):
    # 회전 수
    k = int(input())
    # 톱니 
    wheel = [list(map(int, input().split())) for _ in range(4)]
    # 번호와 방향
    nums = [list(map(int, input().split())) for _ in range(k)]
    
    for n in nums:
        # 방문 확인용
        chk = [0 for _ in range(4)]
        # 번호 (1~4번인데 wheel의 index는 0~3이라 -1함), 방향
        dfs(n[0]-1, n[1])
        
    # 결과
    res = 0
    
    # 화살표가 가리키는 곳을 계산
    for w in range(4):
        res += wheel[w][0] * (2**w)
        
    print("#{} {}".format(tc, res))