## 문자열 압축 *

# 참고 블로그 https://eunhee-programming.tistory.com/135
def new_solution(s):
    # 쪼갠 문자열들의 길이들을 담는 list
    res = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        # 매번 쪼갰을 때 나오는 문자열을 저장
        b = ''
        # 문자열이 연속으로 반복하는지
        cnt = 1
        #그 다음 문자열과 연속되는지 보기 위한 변수
        tmp = s[:i]
        
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
        res.append(len(b))
    
    return min(res)
       
print(new_solution("aabbaccc"))         
'''
 for i in range(1, (len(s)//2)+1)은 쪼갤 수 있는
 최대 길이가 문자열 s의 반
 
 b="aabbaaccc" 같이 홀수인 경우, 
 len(b)=9, len(b)//2 = 4이므로 4가 쪼갤 수 있는 최대 길이
 5씩 쪼개면 10 이상이 되므로 index가 범위를 벗어나 오류.
 

'''









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


def explain(s):
    
    res = len(s) 
    
    # 문자열 길이의 절반을 넘지 않는 범위에서, 
    # 1부터 문자열 길이의 절반까지 반복합니다.
    for x in range(1, len(s) // 2 + 1):
        cur_len = 0 # 현재 압축된 문자열의 길이를 초기화합니다.
        cur_s = '' # 압축한 문자열을 담는 변수를 초기화합니다.
        cnt = 1 # 압축한 문자열의 개수를 세는 변수를 초기화합니다.
        
        # x 길이만큼 쪼갠 문자열을 순회합니다.
        for i in range(0, len(s) + 1, x):
            temp = s[i:i+x] # x 길이만큼 쪼갠 문자열을 저장합니다.
            
            # 압축한 문자열이 같은 경우 개수를 세어줍니다.
            if cur_s == temp : 
                cnt += 1
            
            # 압축한 문자열이 다른 경우
            elif cur_s != temp:
                cur_len += len(temp) # 압축하지 않은 길이를 더합니다.
                
                # 개수가 1이 아닌 경우 개수 길이를 더합니다.
                if cnt > 1 : 
                    cur_len += len(str(cnt))
                cnt = 1 # 개수를 초기화합니다.
                cur_s = temp # 압축한 문자열을 현재 문자열로 설정합니다.
        
        res = min(res, cur_len) # 현재까지의 최소 압축 길이를 업데이트합니다.
        
    return res # 최소 압축 길이를 반환합니다.

print(explain("aabbaccc")) # 결과 : 7
