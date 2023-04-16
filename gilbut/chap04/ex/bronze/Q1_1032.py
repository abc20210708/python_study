## 명렴 프롬프트 (브론즈 1) *

n = int(input())
s = list(input())
s_len = len(s)

for i in range(n - 1):
    b = list(input())
    for j in range(s_len):
        if s[j] != b[j]:
            s[j] = "?"

print(''.join(s))