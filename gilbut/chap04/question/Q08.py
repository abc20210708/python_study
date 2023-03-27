# 튜플

def solution(s):
    res = []
    
    temp = s[2:-2].split("},{")
    temp = sorted(temp, key=lambda x:len(x))
    
    for item in temp:
        item = list(map(int, item.split(",")))
        for value in item:
            if value not in res:
                res.append(value)
    
    return res