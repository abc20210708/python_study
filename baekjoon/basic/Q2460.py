# 지능형 기차 2

res = 0
result = 0
for _ in range(10):
    fir, sec = map(int, input().split())
    res -= fir
    res += sec
    result = max(res, result)
    
print(result)
    