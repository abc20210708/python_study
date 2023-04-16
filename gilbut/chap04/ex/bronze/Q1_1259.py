## 팰린드롬수 (브론즈 1)

while 1:
    s = input()
    if s == "0":
        break
    if s == s[::-1]:
        print("yes")
    else:
        print("no")