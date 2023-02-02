
# 거스름돈

'''
'''

n = 999
coins = [500, 100, 50, 10, 5, 1]

result = 0
for i in coins:
    result += n // i
    n %= i

print(result)
