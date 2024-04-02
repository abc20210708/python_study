## 문제3) 비숍으로부터 도망쳐
#  참고 블로그 https://iwantbaobab.tistory.com/48

def solution(bishops):
    a = [[0] * 9 for _ in range(9)]
    direc = [[-1, 1], [-1, -1], [1, 1], [1, -1]]
    
    for bishop in bishops:
        x = ord(bishop[0]) - ord('A')+1
        y = int(bishop[1])
        a[x][y] = 1
        
        for dx, dy in direc:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if ny > 8 or ny < 1 or nx > 8 or nx < 1:
                    break
                a[nx][ny] = 1 # 비숍이 이동가능한 위치를 1로 채움
                
    res = 0
    
    for x in range(1, 9):
        for y in range(1, 9):
            if not a[x][y]:
                res += 1
    
    return res




bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")