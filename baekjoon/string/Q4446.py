# ROT13(4446) 실버 5
## 참고 블로그 http://anna-in-workplace.tistory.com/43
a = "Ita dotf ni dyca nsaw ecc."
temp = ""
b = "One ring to rule them all."

m = ["a", "i", "y", "e", "o", "u"]
z = ["b", "k", "x", "z", "n", "h", 
        "d", "c", "w", "g", "p", "v",
        "j", "q", "t", "s", "r", "l",
        "m", "f" ]

while 1:
    try:
        s = input()
        res = ""
        for c in s:
            is_lower = True
            
            if c.isupper(): # 대문자면
                is_lower = False
                c = c.lower()
            
            if (c in m):
                change_c = m[(m.index(c)+3) % 6]
                res += (change_c if is_lower else change_c.upper())
            
            elif (c in z):
                change_c = z[(z.index(c)+10) % 20]
                res += (change_c if is_lower else change_c.upper())
            else:
                res += c
        print(res)
    except:
        break