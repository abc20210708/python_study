# ROT13 

target = "One is 1"
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
    elif ord(i) >= 48 and 57 >= ord(i):
        print(i, end="")