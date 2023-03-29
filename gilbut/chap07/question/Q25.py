## 두 개 뽑아서 더하기

def solution(numbers):
    res = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res.append(numbers[i] + numbers[j])
            
    res = set(res)
    res = list(res)
    res.sort()
    
    return res

def solution_1(numbers):
    res = set()
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res.add(numbers[i] + numbers[j])

    return sorted(res)