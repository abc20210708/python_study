## 도비의 난독증 테스트 (브론즈 1)

while 1:
    n = int(input())
    if n == 0: break
    tmp = []
    for _ in range(n):
        s = input()
        tmp.append(s)
    tmp.sort(key=str.lower)
    print(tmp[0])