## 문제8) TV 애청자 A씨 - Python3

def solution(programs):
    
    res = 0
    used_tv = [0] * 25
    
    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] += 1
    
    for i in used_tv:
        if i >= 2:
            res += 1
    return res

print(solution([[1,6], [3,5], [2,8]]))