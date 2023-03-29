## 문자열 내 마음대로 정렬하기

def explain(strings, n):
    # 두 문자열 합치기
    return sorted(sorted(strings), key=lambda x:x[n] + x)

def new_solution(strings, n):
    # 튜플로 만들기
    return sorted(strings, key=lambda x:(x[n], x))