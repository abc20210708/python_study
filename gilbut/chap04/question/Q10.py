## 문자열 압축

# 1. 압축 가능한 길이만큼 (전체의 반) 순회
def explain(s):
    res = len(s)
    for x in range(1, len(s) // 2 + 1):
        comp_len = 0
        comp = ''
        cnt = 1
        for i in range(0, len(s) + 1, x):
            temp = s[i:i+x]
            if comp == temp : cnt += 1
            elif comp != temp:
                comp_len += len(temp)
                if cnt > 1 : comp_len += len(str(cnt))
                cnt = 1
                comp = temp
        res = min(res, comp_len)
        
    return res

print(explain("aabbaccc"))