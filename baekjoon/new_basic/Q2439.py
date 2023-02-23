# 별 찍기 - 2

n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
    
'''
n = int(input())

for i in range(1, n+1):
    num = n - i 
    temp = num * " "
    temp += "*" * i
    print(temp)
'''