# 튜플

def explain(s):
    # 딕셔너리 사용, 중복 검사 시간 O(1)
    res = {}
    s = sorted(s[2:-2].split("},{"), key=len)
    # 쪼갠 문자열을 한 번 더 "," 기준으로 쪼개 숫자 있는 문자 찾기
    for tuples in s:
        elements = tuples.split(",")
        for element in elements:
            num = int(element)
            if num not in res:
                # 딕셔너리 키 사용(값은 아무거나)
                res[num] = 1
    
    # 딕셔너리의 키 값만 배열의 인자가 됨
    return list(res)
                
print(explain("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

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