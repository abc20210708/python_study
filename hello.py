# 민균이의 비밀번호 다시 풀기

n = int(input())
arr = [input() for _ in range(n)]


for i in arr:
    if i[::-1] in arr:
        print(len(i), i[len(i)//2])
        break
    