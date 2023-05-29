## 광물캐기

import sys 

def solution(picks, minerals):
    res = sys.maxsize
    
    visited = [0 for _ in range(3)] # 사용 개수
    orders = []
    def dfs(depth, tired):
        nonlocal res
        
        if depth == sum(picks):
            res = min(res, tired)
            return

        for i in range(3):
            if visited[i] < picks[i]:
                visited[i] += 1
                orders.append(i)
                plus = calc(depth)
                tired += plus
                
                if res > tired:
                    dfs(depth+1, tired)
                visited[i] -= 1
                orders.pop()
                tired -= plus
    
    tired_lst = [
        (1,1,1),
        (5,1,1),
        (25,5,1)    
    ] # 피로도 리스트 
    
    DIA = 0
    IRON = 1
    STONE = 2
    
    def calc(depth):
        plus = 0
        for i in range(depth*5, (depth+1)*5):
            if i >= len(minerals):
                break
            if minerals[i] == "diamond":
                plus += tired_lst[orders[depth]][DIA]
            elif minerals[i] == "iron":
                plus += tired_lst[orders[depth]][IRON]
            elif minerals[i] == "stone":
                plus += tired_lst[orders[depth]][STONE]
        
        return plus
    
    dfs(0,0)
    return res
    
solution([1, 3, 2],
         ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])