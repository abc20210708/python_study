## 종이접기

def solution(grid):
    res = 0
    
    for i in range(4):
        for j in range(4):
            for k in range(j+1, 4, 2):
                res = max(res, max(grid[i][j]+grid[i][k], grid[j][i] + grid[k][i]))
            return res
        
        
solution([[1 ,4 ,16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]])