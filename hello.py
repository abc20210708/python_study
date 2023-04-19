# 튜플 다시 풀기

def solution(s):
    s = sorted(s[2:-2].split("},{"), key=len)
    res = {}
    
    for i in s:
        tmp = i.split(",")
        for j in tmp:
            num = int(j)
            if num not in res:
                res[num] = 1
    
    return list(res)


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))