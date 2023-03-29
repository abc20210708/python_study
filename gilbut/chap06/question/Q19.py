## 모의고사

def solution(answers):
    res = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    arr = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == num1[i % 5]: arr[0] += 1
        if answers[i] == num2[i % 8]: arr[1] += 1
        if answers[i] == num3[i % 10]: arr[2] += 1
    
    
    for i in range(len(arr)):
        if max(arr) == arr[i]:
            res.append(i+1)
    
    res.sort()
    
    return res