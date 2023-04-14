# 도비의 난독증 테스트 다시 풀기

while 1:
    n = int(input())
    if n == 0: break
    arr = []
    for _ in range(n):
        s = input()
        arr.append(s)
    arr.sort(key=str.lower)
    print(arr[0])