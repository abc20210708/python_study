## 문자열 내 마음대로 정렬하기

def explain(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n] + x)

