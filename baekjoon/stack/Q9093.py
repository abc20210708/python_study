# 단어 뒤집기

n = int(input())

for _ in range(n):
    temp = input()
    temp += " "
    stack = []
    for i in temp:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')