## 꽃피우기

from queue import Queue
'''
 참고 블로그 https://velog.io/@iamjinseo/%EC%9D%B4%EC%BD%94%ED%85%8C-%EA%B5%AC%ED%98%84%EC%83%81%ED%95%98%EC%A2%8C%EC%9A%B0-%EC%8B%9C%EA%B0%81-%EC%99%95%EC%8B%A4%EC%9D%98-%EB%82%98%EC%9D%B4%ED%8A%B8-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%AC%EC%A0%95%EB%A0%AC
 '''
def solution(garden):
    answer = 0
    #    동, 서, 남, 북
    dx = [0, 0, 1, -1]  
    dy = [1, -1, 0, 0]

    q = Queue()
    n = len(garden)
    for i in range(n):
        for j in range(n):
            if garden[i][j]==1: 
                q.put((i, j, 0)) #첫날 1있으면 좌표와 일수(0)넣기
    
    while not q.empty():
        x, y, day = q.get() 

        for i in range(4):
            nx = x + dx[i] #다음 스텝
            ny = y + dy[i]
            nday = day + 1 #다음날로 넘기기

            if (nx >=0 and nx <n and ny >=0 and ny<n) and (garden[nx][ny]==0):
                garden[nx][ny] = 1 #꽃피우기
                q.put((nx, ny, nday)) #꽃 위치와 날짜 삽입
                answer = nday #하루 넘긴 날이 정답(여기서 꽃이 다 펴버리면 그다음날에 방문을 못하므로)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)