## 첫 글자를 대문자로 (브론즈 3)

n = int(input())
for _ in range(n):
    s = list(input())
    s[0] = s[0].upper()
    print(''.join(s))
    