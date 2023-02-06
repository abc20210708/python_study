# 정렬 라이브러릴에서 Key를 활용한 소스코드
array = [("바나나", 2), ("사과", 5), ("당근", 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)