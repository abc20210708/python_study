
# 보물 - (실버 4)

'''
참고 블로그 https://yoonsang-it.tistory.com/44
'''
# n = 9

# a = [5, 15, 100, 31, 39, 0, 0, 3, 26]
# b = [11, 12, 13, 2, 3, 4, 5, 9, 1]

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


s = 0

for i in range(n) :
    s += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
    
print(s)
    

