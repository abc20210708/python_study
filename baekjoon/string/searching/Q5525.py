# IOIOI

## 참고 블로그 https://black-hair.tistory.com/135

n = int(input())
m = int(input())
s = input()
p = 'IO' * n + 'I'
res = 0

for i in range(m - len(p)):
    if s[i] == 'I':
        if s[i:i+len(p)] == p:
            res += 1
            
print(res)
