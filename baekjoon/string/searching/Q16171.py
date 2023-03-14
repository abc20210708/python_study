# 나는 친구가 적다 (Small)

s = input()
target = input()
temp = "".join([i for i in s if not i.isdigit()])

if target in temp:
    print(1)
else:
    print(0)

#print(temp)