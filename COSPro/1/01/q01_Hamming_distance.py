## 문제2) 해밍 거리 구하기

def func_a(string, length):
    padZero = ""
    padSize = length - len(string)
    for i in range(padSize):
        padZero += "0"
    return padZero + string


def solution(binaryA, binaryB):
    max_len = max(len(binaryA), len(binaryB))
    binaryA = func_a(binaryA, binaryB)
    bomaryB = func_a(binaryB, binaryA)
    
    diff_distance = 0
    for i in range(max_len):
        if binaryA[i] != binaryB[i]:
            diff_distance += 1
    return diff_distance
    


binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

print("solution 함수의 반환 값은", ret, "입니다.")