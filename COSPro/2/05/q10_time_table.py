## 문제10) 가장 오래 일한 사람을 구해 주세요.

def solution(time_table, n):
    
    tmp = [0] * len(time_table)
    
    for i in range(len(time_table)):
        tmp[i%n] += time_table[i]
    
    return max(tmp)