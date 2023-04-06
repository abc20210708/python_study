## 이진 변환 반복하기

def explain(s):
    change, zero = 0, 0
    
    while s != '1':
        change += 1
        num = s.count("1")
        zero += len(s) - num
        s = bin(num)[2:]
    
    return [change, zero]

print(explain("0111010"))


def solution(s):
    res = [0, 0]
    temp = s
    
    while len(temp) != 1:
        # 이진 변환
        res[0] += 1
        length = len(temp)
        # 0 제거
        temp = temp.replace("0", "")
        res[1] += length - len(temp)
        temp = bin(len(temp))[2:]
    
    return res
    
print(solution("0111010"))