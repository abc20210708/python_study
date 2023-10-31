## 근무 시간 다시 풀기

res = 0

for _ in range(5):
    s1, s2 = input().split(" ")
    h1, m1 = map(int, s1.split(":"))
    h2, m2 = map(int, s2.split(":"))
    
    if m1 > m2 :
        res += ((h2-h1-1)* 60) + (60 -(m1-m2))
    else:
        res += ((h2-h1)* 60) + (m2-m1)
    
print(res)