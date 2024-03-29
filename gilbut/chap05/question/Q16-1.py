## 콜라츠 추측 다른 풀이
def collatz(num):
    if num == 1:
        return 0
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1

def solution(num):
    return collatz(num)