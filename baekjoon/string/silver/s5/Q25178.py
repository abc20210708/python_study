## 두루마리 휴지 (실버 5)

n = int(input())

s1 = input().rstrip()
s2 = input().rstrip()

tmp1 = set(s1)
tmp2 = set(s2)

if tmp1 != tmp2:
    print("NO")
    exit()
if s1[0] != s2[0] or s1[-1] != s2[-1]:
    print("NO")
    exit()
    
tmp1.remove("a")
tmp2.remove("a")
tmp1.remove("e")
tmp2.remove("e")
tmp1.remove("i")
tmp2.remove("i")
tmp1.remove("o")
tmp2.remove("o")
tmp1.remove("u")
tmp2.remove("u")

if tmp1 != tmp2:
    print("NO")
    exit()
else:
    print("YES")