## 두 개 뽑아서 더하기

from itertools import combinations

def explain(numbers):
    res = set()
    selects = list(combinations(numbers, 2))
    for select in selects:
        (a, b) = select
        res.add(a + b)
    
    return sorted(res)

print(explain([2, 1, 3, 4, 1]))

def new_solution(numbers):
    return sorted(set(map(sum, combinations(numbers, 2))))


def solution_1(numbers):
    res = set()
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res.add(numbers[i] + numbers[j])

    return sorted(res)

def solution(numbers):
    res = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res.append(numbers[i] + numbers[j])
            
    res = set(res)
    res = list(res)
    res.sort()
    
    return res