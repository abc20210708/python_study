# 같은 숫자는 싫어

def solution(arr):
    res = []
    first = arr[0]
    res.append(arr[0])
    
    for i in range(1, len(arr)):
        if first != arr[i]:
            res.append(arr[i])
            first = arr[i]
    
    return res

'''
def solution(arr):
    res = []
    
    
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            res.append(arr[i])
            
    res.append(arr[len(arr)-1])
    
    return res
'''