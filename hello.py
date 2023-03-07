# 보물 다시 풀기

'''
5
1 1 1 6 0
2 7 8 3 1
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0

for i in range(n):
    s += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
    
print(s)