## 경고 (브론즈 3) *

#h1, m1, s1 = map(int, input().split(":"))
#h2, m2, s2 = map(int, input().split(":"))
h1, m1, s1 = map(int, "12:34:56".split(":"))
h2, m2, s2 = map(int, "14:36:22".split(":"))

t1 = h1* 60 * 60  + m1 * 60 + s1
t2 = h2* 60 * 60  + m2 * 60 + s2

t = t2 - t1 if t2 > t1 else t2 - t1 + 24 * 60 * 60

h = t // 60 // 60
m = t // 60 % 60
s = t % 60

print("%02d:%02d:%02d" % (h, m, s))

'''
a, b, c = map(int,input().split('.'))
print('%04d.%02d.%02d' % (a,b,c))
# 입력 : 2020.8.20
# 출력 : 2020.08.20

# 참고 블로그 https://hyjykelly.tistory.com/65
'''

    

first = list(map(int, input().split(":")))
second = list(map(int, input().split(":")))

if first[2] > second[2]:
    s = 60 - first[2] + second[2]
    first[1] += 1
else: 
    s = second[2] - first[2]
    
if first[1] > second[1]:
    m = 60 - first[1] + second[1]
    first[0] += 1
else:
    m = second[1] - first[1]
    
if first[0] > second[0]:
    h = 24 - first[0] + second[0]
else:
    h = second[0] - first[0]
    
if first[0] == second[0] and first[1] == second[1] and first[2] == second[2]:
    h = 24
    m = 0
    s = 0
    
print("%02d:%02d:%02d" % (h, m, s))
    