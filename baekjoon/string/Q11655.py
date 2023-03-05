
target = "Baekjoon Online Judge"
temp = ""

for i in target:
    if i == " ":
        print(" ", end="")
    elif i.islower():
        temp = ord(i) + 13
        if temp > 122:
            temp -= 26
        print(chr(temp), end="")
    elif i.isupper():
        temp = ord(i) + 13
        if temp > 90:
            temp -= 26
        print(chr(temp), end="")