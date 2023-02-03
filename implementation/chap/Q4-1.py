
# 상하좌우

'''
'''




'''
n = 5

a = 1
b = 1

walk = ["R", "R", "R", "U", "D", "D"]

min_walk = 1
max_walk = n

for i in walk:
    if b < n and i == "R":
        b += 1
    elif b >= 2 and i == "L":
        b -= 1
    elif a >= 2 and i == "U":
        a -= 1
    elif a < n and i == "D":
        a += 1

print(a, b)
'''