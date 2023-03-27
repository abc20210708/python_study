## 문자열 압축

def compress(s, length):
    words = [s[i:i+length] for i in range(0, len(s), length)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for pattern, compare in zip(words, words[1:] + ['']):
        if pattern == compare : cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = compare
            cur_cnt = 1
    return sum(len(words) + (len(str(cnt)) if cnt > 1 else 0) for words, cnt in res)

def new_solution(s):
    if len(s) == 1: return 1
    else: return min(compress(s, length) for length in list(range(1, len(s)// 2 + 1)))


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