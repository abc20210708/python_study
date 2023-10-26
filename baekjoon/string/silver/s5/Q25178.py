## 두루마리 휴지 (실버 5)
#  참고 블로그 https://tooy.tistory.com/71

n = int(input())

s1 = input().rstrip()
s2 = input().rstrip()

n1, n2, n3 = False, False, False

if sorted(s1) == sorted(s2):
    n1 = True

if s1[0] == s2[0] and s1[-1] == s2[-1]:
    n2 = True
    
for i in 'aeiou':
    s1 = s1.replace(i, '')
    s2 = s2.replace(i, '')

if s1 == s2:
    n3 = True

if n1 and n2 and n3:
    print("YES")
else:
    print("NO")