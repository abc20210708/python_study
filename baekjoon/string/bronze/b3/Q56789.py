## 한다 안한다 (브론즈 3)

t = int(input())

for _ in range(t):
    s = input()
    idx = len(s) // 2
    if s[idx-1] == s[idx]:
        print("Do-it")
    else:
        print("Do-it-Not")